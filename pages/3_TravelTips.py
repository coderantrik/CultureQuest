import streamlit as st
from utils.ui_helpers import set_background

set_background()

def show_travel_tips():
    # Title with dark background and white text
    st.markdown(
        """
        <div style='
            background-color: #2c3e50;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 25px;
        '>
            <h1 style='
                color: white;
                text-align: center;
                font-family: Arial, sans-serif;
                margin: 0;
            '>📚 Travel Tips for Responsible Tourism</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p style='
            text-align: center; 
            font-size: 18px; 
            font-family: Arial, sans-serif;
            margin-bottom: 30px;
            color: white;
        '>
        Embrace the culture, respect the environment, and leave a positive impact on your travels.
        </p>
        """,
        unsafe_allow_html=True
    )

    tips = [
        {"icon": "🌿", "tip": "Respect local customs and traditions."},
        {"icon": "♻️", "tip": "Minimize plastic usage and carry reusable items."},
        {"icon": "🗣️", "tip": "Learn basic greetings in local languages."},
        {"icon": "📷", "tip": "Always ask before photographing locals."},
        {"icon": "🚶", "tip": "Explore on foot or with local guides."},
        {"icon": "🛍️", "tip": "Support local artisans and businesses."},
        {"icon": "💧", "tip": "Conserve water and electricity during your stay."},
        {"icon": "🗑️", "tip": "Dispose of waste responsibly and recycle when possible."},
    ]

    for i, item in enumerate(tips, start=1):
        with st.expander(f"{item['icon']} Tip {i}"):
            st.markdown(
                f"""
                <p style='
                    font-family: Arial, sans-serif;
                    font-size: 16px;
                    color: #2c3e50;
                '>{item['tip']}</p>
                """,
                unsafe_allow_html=True
            )

if __name__ == "__main__":
    show_travel_tips()
