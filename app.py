import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Flights Analytics",
    page_icon="✈",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f8fafc;
    }

    .block-container {
        padding-top: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
        max-width: 1400px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Landing Page */

    .hero {
        padding: 45px 10px 30px 10px;
    }

    .tag {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 20px;
        background-color: #e0f2fe;
        color: #0369a1;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1px;
        margin-bottom: 18px;
    }

    .hero-title {
        font-size: 52px;
        font-weight: 800;
        line-height: 1.1;
        color: #0f172a;
        margin-bottom: 18px;
    }

    .hero-title span {
        color: #2563eb;
    }

    .hero-text {
        font-size: 17px;
        line-height: 1.7;
        color: #64748b;
        max-width: 720px;
    }

    .info-card {
        padding: 25px;
        border-radius: 16px;
        background-color: white;
        border: 1px solid #e2e8f0;
        min-height: 180px;
        box-shadow: 0 4px 15px rgba(15, 23, 42, 0.04);
    }

    .info-card:hover {
        border-color: #93c5fd;
    }

    .number {
        color: #2563eb;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 1px;
        margin-bottom: 15px;
    }

    .info-card h3 {
        color: #0f172a;
        font-size: 20px;
        margin-bottom: 10px;
    }

    .info-card p {
        color: #64748b;
        line-height: 1.6;
        font-size: 14px;
    }

    .tech-box {
        margin-top: 35px;
        padding: 30px;
        border-radius: 18px;
        background-color: #eff6ff;
        border: 1px solid #dbeafe;
    }

    .tech-box h2 {
        color: #0f172a;
    }

    .tech-box p {
        color: #64748b;
        line-height: 1.7;
    }

    /* KPI Cards */

    .kpi-card {
        background-color: white;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.04);
    }

    .kpi-title {
        color: #64748b;
        font-size: 13px;
        margin-bottom: 8px;
    }

    .kpi-value {
        color: #0f172a;
        font-size: 28px;
        font-weight: 700;
    }

    /* Footer */

    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        margin-top: 50px;
        padding: 20px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# DATABASE CONNECTION
# =========================================================

db = DB()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    """
    <div style="
        font-size:24px;
        font-weight:800;
        margin-bottom:5px;
    ">
        FLIGHT ANALYTICS
    </div>

    <div style="
        font-size:13px;
        color:#94a3b8 !important;
        margin-bottom:25px;
    ">
        Data Intelligence Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

user_option = st.sidebar.selectbox(
    "Navigation",
    [
        "Select One",
        "Check Flights",
        "Analytics"
    ]
)


# =========================================================
# LANDING PAGE
# =========================================================

if user_option == "Select One":

    col1, col2 = st.columns([1.15, 0.85])

    with col1:

        st.markdown("""
        <div class="hero">

            <div class="tag">
                FLIGHT DATA INTELLIGENCE
            </div>

            <div class="hero-title">
                Explore Flights.<br>
                <span>Discover Insights.</span>
            </div>

            <div class="hero-text">
                An interactive flight analytics platform that transforms
                raw flight data into meaningful insights. Explore airlines,
                routes, airports and daily flight patterns through
                interactive visualizations.
            </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div style="
            height:380px;
            border-radius:25px;
            background:linear-gradient(135deg,#0f172a,#1e3a8a);
            position:relative;
            overflow:hidden;
            margin-top:40px;
        ">

            <div style="
                position:absolute;
                width:350px;
                height:350px;
                border:1px solid rgba(255,255,255,0.15);
                border-radius:50%;
                right:-100px;
                top:10px;
            "></div>

            <div style="
                position:absolute;
                width:260px;
                height:260px;
                border:1px solid rgba(255,255,255,0.12);
                border-radius:50%;
                right:-50px;
                top:55px;
            "></div>

            <div style="
                position:absolute;
                font-size:55px;
                top:130px;
                left:42%;
                transform:rotate(-20deg);
            ">
                ✈
            </div>

            <div style="
                position:absolute;
                width:280px;
                border-top:2px dashed rgba(147,197,253,0.7);
                transform:rotate(-25deg);
                top:190px;
                left:50px;
            "></div>

            <div style="
                position:absolute;
                bottom:60px;
                left:35px;
                color:white;
                font-size:13px;
                font-weight:600;
            ">
                DEL · Delhi
            </div>

            <div style="
                position:absolute;
                top:65px;
                right:35px;
                color:white;
                font-size:13px;
                font-weight:600;
            ">
                BOM · Mumbai
            </div>

        </div>
        """, unsafe_allow_html=True)


    st.markdown("### What can you explore?")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="info-card">

            <div class="number">01 — SEARCH</div>

            <h3>Flight Search</h3>

            <p>
                Find available flights between different source
                and destination cities and explore important
                flight details.
            </p>

        </div>
        """, unsafe_allow_html=True)


    with col2:

        st.markdown("""
        <div class="info-card">

            <div class="number">02 — ANALYSIS</div>

            <h3>Airline Insights</h3>

            <p>
                Understand airline frequency and identify
                which airlines operate the highest number
                of flights.
            </p>

        </div>
        """, unsafe_allow_html=True)


    with col3:

        st.markdown("""
        <div class="info-card">

            <div class="number">03 — TRENDS</div>

            <h3>Airport & Trends</h3>

            <p>
                Discover busy airports and analyze daily
                flight patterns through interactive charts.
            </p>

        </div>
        """, unsafe_allow_html=True)


    st.markdown("""
    <div class="tech-box">

        <h2>Built with Data & Technology</h2>

        <p>
            The application uses MySQL for data storage and SQL-based
            analysis, Python for data processing, Streamlit for the
            interactive interface and Plotly for data visualization.
        </p>

    </div>
    """, unsafe_allow_html=True)


    st.markdown("### How it works")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        **01 — DATA**

        Flight records are stored and managed in MySQL.
        """)

    with col2:
        st.markdown("""
        **02 — QUERY**

        SQL queries retrieve and analyze the required information.
        """)

    with col3:
        st.markdown("""
        **03 — INSIGHTS**

        Plotly converts the analysis into interactive visualizations.
        """)


# =========================================================
# CHECK FLIGHTS
# =========================================================

elif user_option == "Check Flights":

    st.title("✈️ Check Flights")

    st.markdown(
        "Search flights by selecting your source and destination."
    )

    city = db.fetch_city_names()

    if city:

        col1, col2 = st.columns(2)

        with col1:
            source = st.selectbox(
                "Source",
                sorted(city)
            )

        with col2:
            destination = st.selectbox(
                "Destination",
                sorted(city)
            )

        st.write("")

        if st.button("Search Flights", use_container_width=True):

            if source == destination:

                st.warning(
                    "Source and destination cannot be the same."
                )

            else:

                results = db.fetch_all_flights(
                    source,
                    destination
                )

                if results:

                    st.success(
                        f"{len(results)} flight(s) found."
                    )

                    st.dataframe(
                        results,
                        use_container_width=True,
                        hide_index=True
                    )

                else:

                    st.info(
                        "No flights found for this route."
                    )

    else:

        st.error(
            "Unable to retrieve city information from database."
        )


# =========================================================
# ANALYTICS
# =========================================================

elif user_option == "Analytics":

    st.title("📊 Flight Analytics")

    st.markdown(
        "Explore flight frequency, airport activity and daily trends."
    )

    st.write("")


    # -----------------------------------------------------
    # AIRLINE DATA
    # -----------------------------------------------------

    airline, frequency = db.fetch_airline_frequency()


    # -----------------------------------------------------
    # AIRPORT DATA
    # -----------------------------------------------------

    city, frequency1 = db.busy_airport()


    # -----------------------------------------------------
    # DAILY DATA
    # -----------------------------------------------------

    date, frequency2 = db.daily_frequency()


    # -----------------------------------------------------
    # KPI CARDS
    # -----------------------------------------------------

    total_flights = sum(frequency)
    total_airlines = len(airline)
    total_airports = len(city)

    if frequency2:

        avg_daily_flights = round(
            sum(frequency2) / len(frequency2),
            1
        )

    else:

        avg_daily_flights = 0


    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(f"""
        <div class="kpi-card">

            <div class="kpi-title">
                TOTAL FLIGHTS
            </div>

            <div class="kpi-value">
                {total_flights:,}
            </div>

        </div>
        """, unsafe_allow_html=True)


    with col2:

        st.markdown(f"""
        <div class="kpi-card">

            <div class="kpi-title">
                AIRLINES
            </div>

            <div class="kpi-value">
                {total_airlines}
            </div>

        </div>
        """, unsafe_allow_html=True)


    with col3:

        st.markdown(f"""
        <div class="kpi-card">

            <div class="kpi-title">
                AIRPORTS
            </div>

            <div class="kpi-value">
                {total_airports}
            </div>

        </div>
        """, unsafe_allow_html=True)


    with col4:

        st.markdown(f"""
        <div class="kpi-card">

            <div class="kpi-title">
                AVG. FLIGHTS / DAY
            </div>

            <div class="kpi-value">
                {avg_daily_flights}
            </div>

        </div>
        """, unsafe_allow_html=True)


    st.write("")
    st.write("")


    # =====================================================
    # AIRLINE + AIRPORT
    # =====================================================

    col1, col2 = st.columns(2)


    # -----------------------------------------------------
    # AIRLINE PIE CHART
    # -----------------------------------------------------

    with col1:

        st.subheader("Flights by Airline")

        fig = go.Figure(
            go.Pie(
                labels=airline,
                values=frequency,
                hole=0.45,
                hoverinfo="label+percent",
                textinfo="percent"
            )
        )

        fig.update_layout(
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),
            showlegend=True
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # -----------------------------------------------------
    # BUSIEST AIRPORTS
    # -----------------------------------------------------

    with col2:

        st.subheader("Busiest Airports")

        fig = px.bar(
            x=frequency1[:10],
            y=city[:10],
            orientation="h",
            labels={
                "x": "Number of Flights",
                "y": "Airport"
            }
        )

        fig.update_layout(
            yaxis=dict(
                categoryorder="total ascending"
            ),
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # =====================================================
    # DAILY FLIGHT TREND
    # =====================================================

    st.subheader("Daily Flight Trend")

    fig = px.line(
        x=date,
        y=frequency2,
        labels={
            "x": "Date",
            "y": "Number of Flights"
        }
    )

    fig.update_layout(
        hovermode="x unified",
        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # =====================================================
    # FOOTER
    # =====================================================

    st.markdown("""
    <div class="footer">
        Flight Analytics Dashboard · Python · MySQL · Streamlit · Plotly
    </div>
    """, unsafe_allow_html=True)