# utils/ui_helpers.py

def set_background():
    import streamlit as st
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://i.postimg.cc/6qTc0wBB/3.png");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            background-attachment: fixed;
        }}
        .main > div {{
            background-color: rgba(0, 0, 0, 0.6);
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 0 15px rgba(255,255,255,0.1);
            color: #f0e6d2;
        }}
        h1, h2, h3 {{
            color: #ffdf91;
            text-shadow: 1px 1px 2px #000;
        }}
        p {{
            font-size: 1.1rem;
            color: #eaeaea;
        }}
        strong {{
            color: #ffd700;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
