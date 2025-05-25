import streamlit as st
import pandas as pd
import altair as alt
from utils.snowflake_connection import create_connection
from utils.ui_helpers import set_background
import pydeck as pdk

set_background()

st.title("🎨 Explore Cultural Sites")

# Connect and load data
conn = create_connection()
df = pd.read_sql("SELECT * FROM CULTURAL_SITES;", conn)
df.columns = df.columns.str.strip().str.upper()

# Convert visitor count to numeric safely
df["VISITOR_COUNT"] = pd.to_numeric(df["VISITOR_COUNT"], errors="coerce")

# Sidebar Filters
st.sidebar.header("🔍 Filter Cultural Experiences")

state_filter = st.sidebar.multiselect(
    "Choose State(s):",
    options=sorted(df["STATE"].dropna().unique()),
    default=sorted(df["STATE"].dropna().unique()),
)

category_filter = st.sidebar.multiselect(
    "Select Category:",
    options=sorted(df["CATEGORY"].dropna().unique()),
    default=sorted(df["CATEGORY"].dropna().unique()),
)

month_filter = st.sidebar.text_input(
    "Best Month to Visit (e.g., November):",
    placeholder="Type a month name"
)

# Apply filters
filtered_df = df[
    (df["STATE"].isin(state_filter)) & 
    (df["CATEGORY"].isin(category_filter))
]

if month_filter.strip():
    filtered_df = filtered_df[
        filtered_df["BEST_MONTHS"].str.contains(month_filter, case=False, na=False)
    ]

# Summary Stats
st.markdown(f"""
**🎯 {len(filtered_df)} Cultural Sites Found**  
🧭 States: {', '.join(sorted(filtered_df['STATE'].unique()))}  
🏷️ Categories: {', '.join(sorted(filtered_df['CATEGORY'].unique()))}
""")

# ✅ Show as styled cards
st.subheader("🧳 Cultural Experiences")

for _, row in filtered_df.iterrows():
    st.markdown(f"""
    <div style="
        background: #1e1e1e; 
        color: #f2f2f2; 
        padding: 20px; 
        border-radius: 10px; 
        margin-bottom: 15px; 
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    ">
        <h3 style="margin-bottom: 10px;">🎭 {row['NAME']}</h3>
        <p><strong>📍 State:</strong> {row['STATE']} | <strong>🏷️ Category:</strong> {row['CATEGORY']}</p>
        <p><strong>📅 Best Months:</strong> {row['BEST_MONTHS']}</p>
        <p><strong>👥 Visitors Last Year:</strong> {int(row['VISITOR_COUNT']) if pd.notnull(row['VISITOR_COUNT']) else "N/A"}</p>
        <p style="font-style: italic; color: #ccc;">{row.get('DESCRIPTION', 'No description available.')}</p>
    </div>
    """, unsafe_allow_html=True)

# ✅ Bar Chart - Top Visitor Count Sites
if not filtered_df.empty and filtered_df["VISITOR_COUNT"].notnull().any():
    st.subheader("📊 Visitor Count by Site")
    st.write("Tap Maximize to view full chart")

    # Prepare chart data
    chart_df = (
        filtered_df[["NAME", "STATE", "VISITOR_COUNT"]]
        .dropna(subset=["VISITOR_COUNT"])
        .sort_values("VISITOR_COUNT", ascending=False)
        .head(15)
    )

    # Explicitly convert VISITOR_COUNT to numeric
    chart_df["VISITOR_COUNT"] = pd.to_numeric(chart_df["VISITOR_COUNT"], errors="coerce")

    # Fallback: if still no values, show a message
    if chart_df["VISITOR_COUNT"].isna().all():
        st.warning("⚠️ Visitor count data is missing or not numeric.")
    else:
        chart = alt.Chart(chart_df).mark_bar(size=25, color="#ff884d").encode(
            x=alt.X("VISITOR_COUNT:Q", title="Visitors"),
            y=alt.Y("NAME:N", sort="-x", title=None),
            tooltip=[
                alt.Tooltip("NAME:N", title="Site"),
                alt.Tooltip("STATE:N", title="State"),
                alt.Tooltip("VISITOR_COUNT:Q", title="Visitors", format=",.0f"),
            ]
        ).properties(
            width=700,
            height=30 * len(chart_df),
            title="🔝 Top 15 Sites by Visitors"
        )

        st.altair_chart(chart, use_container_width=True)
else:
    st.info("ℹ️ No visitor count data to display a chart.")


# ✅ Optional Map if location columns exist


# Ensure 'LATITUDE', 'LONGITUDE', 'NAME' exist
if {'LATITUDE', 'LONGITUDE', 'NAME'}.issubset(filtered_df.columns):
    map_data = filtered_df[["LATITUDE", "LONGITUDE", "NAME", "STATE", "CATEGORY"]].dropna()

    if not map_data.empty:
        st.subheader("🗺️ Explore Sites on Map")

        # PyDeck map with tooltips
        layer = pdk.Layer(
            "ScatterplotLayer",
            data=map_data,
            get_position="[LONGITUDE, LATITUDE]",
            get_radius=50000,
            get_fill_color=[255, 136, 77, 180],  # orange semi-transparent
            pickable=True,
        )

        tooltip = {
            "html": "<b>{NAME}</b><br/>📍 {STATE}<br/>🏷️ {CATEGORY}",
            "style": {
                "backgroundColor": "#222",
                "color": "white",
                "fontSize": "14px"
            }
        }

        view_state = pdk.ViewState(
            latitude=map_data["LATITUDE"].mean(),
            longitude=map_data["LONGITUDE"].mean(),
            zoom=4.5,
            pitch=0
        )

        st.pydeck_chart(pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            tooltip=tooltip
        ))
    else:
        st.info("ℹ️ No valid coordinates found to plot the map.")
