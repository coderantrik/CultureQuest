# app/Trends.py

import streamlit as st
import pandas as pd
import altair as alt
from utils.snowflake_connection import create_connection
from utils.ui_helpers import set_background
set_background()

# --- Custom Styling ---
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: #fefefe;
        margin-top: -30px;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #dddddd;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

# --- Title & Subtitle ---
st.markdown("<h1 class='main-title'>📊 Tourism Trends</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Track how tourism flows across India's vibrant states — month by month.</div>", unsafe_allow_html=True)

# --- Data Loading ---
conn = create_connection()

@st.cache_data
def load_tourism_trends():
    query = "SELECT * FROM TOURISM_TRENDS;"
    df = pd.read_sql(query, conn)
    df.columns = df.columns.str.upper()
    return df

trend_df = load_tourism_trends()

# --- Top 5 States Display ---
st.subheader("🔝 Top 5 States by Total Visitors")
top_states = (
    trend_df.groupby("STATE")["AVG_VISITOR_COUNT"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
    .reset_index()
)
st.dataframe(top_states.style.background_gradient(cmap="Oranges"), use_container_width=True)

# --- State Selector ---
selected_state = st.selectbox("📍 Choose a state to explore its monthly tourism trend:", trend_df['STATE'].unique())

# --- Filter and Sort Data ---
chart_data = trend_df[trend_df["STATE"] == selected_state]

# Optional: Ensure month order is correct
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
chart_data["MONTH"] = pd.Categorical(chart_data["MONTH"], categories=month_order, ordered=True)
chart_data = chart_data.sort_values("MONTH")

# --- Altair Line Chart ---
line_chart = alt.Chart(chart_data).mark_line(point=alt.OverlayMarkDef(color="#ff884d", size=70)).encode(
    x=alt.X('MONTH:N', title="Month"),
    y=alt.Y('AVG_VISITOR_COUNT:Q', title='Average Visitor Count'),
    tooltip=[
        alt.Tooltip('MONTH:N', title='Month'),
        alt.Tooltip('AVG_VISITOR_COUNT:Q', title='Visitors', format=',')
    ]
).properties(
    width=700,
    height=400,
    title=f"📈 Monthly Tourism Trend — {selected_state}"
).configure_title(
    fontSize=20,
    font='Inter',
    anchor='start',
    color='#ffffff'
).configure_axis(
    labelColor='#dddddd',
    titleColor='#ffffff'
)

st.altair_chart(line_chart, use_container_width=True)

# --- 📊 Visitor Growth Indicator ---

if len(chart_data) >= 2:
    latest_month = chart_data.iloc[-1]
    previous_month = chart_data.iloc[-2]

    latest_visitors = latest_month["AVG_VISITOR_COUNT"]
    previous_visitors = previous_month["AVG_VISITOR_COUNT"]

    delta = latest_visitors - previous_visitors
    delta_percent = (delta / previous_visitors) * 100 if previous_visitors else 0

    st.markdown("### 📈 Recent Growth Trend")
    st.metric(
        label=f"From {previous_month['MONTH']} to {latest_month['MONTH']}",
        value=f"{int(latest_visitors):,} visitors",
        delta=f"{delta_percent:+.2f}%",
        delta_color="normal"  # or "inverse" / "off"
    )
else:
    st.info("Not enough monthly data to calculate growth.")
st.caption("Monthly change in tourism based on average visitors.")
