import streamlit as st
import pandas as pd
from utils.snowflake_connection import create_connection
from utils.ui_helpers import set_background

# ✅ Streamlit page config
st.set_page_config(
    page_title="CultureQuest 🇮🇳",
    page_icon="🎨",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ✅ Hide Streamlit's default footer and header
st.markdown("""
<style>
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {padding-top: 0;}
</style>
""", unsafe_allow_html=True)

set_background()

# ✅ Main Title & Subheader (centered and styled) — moved above banner image
st.markdown(
    """
    <h1 style='text-align: center; font-size: 3.2rem; font-weight: bold; margin-bottom: 10px;'>
        CultureQuest 🇮🇳
    </h1>
    <h3 style='text-align: center; font-weight: normal; color: #f2f2f2; margin-top: 0; margin-bottom: 20px;'>
        Experience the Soul of India — Beyond Landmarks.
    </h3>
    """,
    unsafe_allow_html=True
)

# ✅ Top banner image — now after the title
st.markdown(
    """
    <style>
    .top-banner {
        width: 100%;
        height: auto;
        margin-bottom: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    </style>
    <img src="https://i.postimg.cc/PqgdhfFR/Chat-GPT-Image-May-25-2025-11-35-56-AM.png" class="top-banner">
    """,
    unsafe_allow_html=True
)

# ✅ Sidebar content with icons
st.sidebar.markdown("## 🎨 CultureQuest")
st.sidebar.markdown("Navigate through India’s diverse cultural canvas:")

st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📍 Quick Links
- 🧭 [Home](./)
- 🏔️ [Hidden Gems](./HiddenGems)
- 📈 [Tourism Trends](./Trends)
- 📚 [Cultural Facts](./Cultural_Facts)
- 🌿 [Travel Tips](./TravelTips)
""", unsafe_allow_html=True)

# ✅ Home Page Description
st.markdown(
    """
            
            
Welcome to **CultureQuest**, your gateway to the timeless legacy of Indian culture and heritage.  
From sacred traditions to modern-day marvels, embark on a journey that blends **history, diversity, and storytelling**—the data-first way!  

🔍 Explore hidden cultural gems  
🎨 Discover vibrant art forms from every region  
📊 Visualize tourism trends with real-time data  
🌱 Learn sustainable travel practices  
🌍 Celebrate the spirit of **Incredible India** with every click  
""")
