import streamlit as st
import pandas as pd
import pydeck as pdk
from utils.snowflake_connection import create_connection
from utils.ui_helpers import set_background

set_background()

# Styled page title with background
st.markdown("""
<div style='
    background: linear-gradient(90deg, #ff9966, #ff5e62);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0 4px 10px rgba(255,94,98,0.5);
'>
    <h1 style='color: white; font-weight: 700; margin: 0;'>🗺️ Hidden Cultural Gems</h1>
    <p style='color: #ffe6e1; font-size: 18px; margin-top: 5px;'>Explore lesser-known but culturally rich destinations across India.</p>
</div>
""", unsafe_allow_html=True)

# Connect and fetch data
conn = create_connection()
df = pd.read_sql("SELECT * FROM CULTURAL_SITES;", conn)
df.columns = df.columns.str.strip().str.upper()

# Sidebar filter for State
states = df['STATE'].dropna().unique()
selected_states = st.sidebar.multiselect("Filter by State(s)", options=sorted(states), default=sorted(states))

filtered_df = df[df['STATE'].isin(selected_states)] if selected_states else df

# Drop rows without geo coordinates
map_data = filtered_df.dropna(subset=['LATITUDE', 'LONGITUDE'])

if map_data.empty:
    st.warning("No cultural sites found for the selected state(s). Please try another selection.")
else:
    # Setup pydeck layer with radius scaling by importance if column exists, else fixed radius
    if 'IMPORTANCE' in map_data.columns:
        # Normalize importance for radius scaling
        imp_min = map_data['IMPORTANCE'].min()
        imp_max = map_data['IMPORTANCE'].max()
        map_data['radius'] = map_data['IMPORTANCE'].apply(lambda x: 5000 + 25000 * (x - imp_min) / (imp_max - imp_min) if imp_max != imp_min else 10000)
    else:
        map_data['radius'] = 10000

    layer = pdk.Layer(
        'ScatterplotLayer',
        data=map_data,
        get_position='[LONGITUDE, LATITUDE]',
        get_radius='radius',
        get_fill_color='[255, 99, 71, 180]',
        pickable=True,
        auto_highlight=True,
    )

    # Set view centered on mean coords or default center of India
    if not map_data.empty:
        latitude = map_data['LATITUDE'].mean()
        longitude = map_data['LONGITUDE'].mean()
    else:
        latitude, longitude = 20.5937, 78.9629  # India center

    view_state = pdk.ViewState(
        latitude=latitude,
        longitude=longitude,
        zoom=5,
        pitch=30
    )

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/streets-v11',
        initial_view_state=view_state,
        layers=[layer],
        tooltip={
            "html": "<b>{NAME}</b><br>State: {STATE}<br>Description: {DESCRIPTION}",
            "style": {"color": "white"}
        }
    ))

    # Add a data table with key info
    st.markdown("### 📋 Explore Cultural Sites")
    display_cols = ['NAME', 'STATE', 'DISTRICT', 'DESCRIPTION']
    if 'DISTRICT' not in map_data.columns:
        display_cols = ['NAME', 'STATE', 'DESCRIPTION']
    st.dataframe(map_data[display_cols].fillna("N/A").reset_index(drop=True), use_container_width=True)
