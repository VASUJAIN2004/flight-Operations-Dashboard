import mysql.connector
import streamlit as st


class DB:

    def __init__(self):

        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="Vasu@2004",
                database="flights"

            )

            self.mycursor = self.conn.cursor()

            print("Database connection established")

        except mysql.connector.Error as e:

            st.error(f"Database connection error: {e}")

            self.conn = None
            self.mycursor = None


    # =====================================================
    # FETCH CITY NAMES
    # =====================================================

    def fetch_city_names(self):

        if self.mycursor is None:
            return []

        query = """
            SELECT DISTINCT Destination
            FROM flights

            UNION

            SELECT DISTINCT Source
            FROM flights
        """

        self.mycursor.execute(query)

        data = self.mycursor.fetchall()

        city = [item[0] for item in data]

        return city


    # =====================================================
    # FETCH FLIGHTS
    # =====================================================

    def fetch_all_flights(self, source, destination):

        if self.mycursor is None:
            return []

        query = """
            SELECT
                Airline,
                Route,
                Dep_Time,
                Duration,
                Price
            FROM flights
            WHERE Source = %s
            AND Destination = %s
        """

        self.mycursor.execute(
            query,
            (source, destination)
        )

        data = self.mycursor.fetchall()

        return data


    # =====================================================
    # AIRLINE FREQUENCY
    # =====================================================

    def fetch_airline_frequency(self):

        if self.mycursor is None:
            return [], []

        query = """
            SELECT
                Airline,
                COUNT(*) AS frequency
            FROM flights
            GROUP BY Airline
            ORDER BY frequency DESC
        """

        self.mycursor.execute(query)

        data = self.mycursor.fetchall()

        airline = []
        frequency = []

        for item in data:

            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency


    # =====================================================
    # BUSIEST AIRPORTS
    # =====================================================

    def busy_airport(self):

        if self.mycursor is None:
            return [], []

        query = """
            SELECT
                airport,
                COUNT(*) AS frequency
            FROM
            (
                SELECT Source AS airport
                FROM flights

                UNION ALL

                SELECT Destination AS airport
                FROM flights
            ) AS airport_data

            GROUP BY airport
            ORDER BY frequency DESC
        """

        self.mycursor.execute(query)

        data = self.mycursor.fetchall()

        city = []
        frequency = []

        for item in data:

            city.append(item[0])
            frequency.append(item[1])

        return city, frequency


    # =====================================================
    # DAILY FLIGHT FREQUENCY
    # =====================================================

    def daily_frequency(self):

        if self.mycursor is None:
            return [], []

        query = """
            SELECT
                Date_of_Journey,
                COUNT(*) AS frequency
            FROM flights
            GROUP BY Date_of_Journey
            ORDER BY Date_of_Journey
        """

        self.mycursor.execute(query)

        data = self.mycursor.fetchall()

        date = []
        frequency = []

        for item in data:

            date.append(item[0])
            frequency.append(item[1])

        return date, frequency


    # =====================================================
    # CLOSE CONNECTION
    # =====================================================

    def close_connection(self):

        if self.conn:

            self.mycursor.close()
            self.conn.close()

            print("Database connection closed")