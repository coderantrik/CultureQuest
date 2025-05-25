import streamlit as st

cultural_facts = [
    {"fact": "India has the largest number of post offices in the world.", "icon": "📮"},
    {"fact": "The game of chess originated in India.", "icon": "♟️"},
    {"fact": "Yoga was invented in India over 5,000 years ago.", "icon": "🧘‍♂️"},
    {"fact": "The Indian film industry produces the largest number of films annually.", "icon": "🎬"},
    {"fact": "Kumbh Mela is the largest religious gathering in the world.", "icon": "🙏"},
    {"fact": "India is home to the world's first university, Nalanda, dating back to 5th century AD.", "icon": "🏫"},
]

def show_cultural_facts():
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
            '>Cultural Facts about India 🇮🇳</h1>
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
        '>
        Discover fascinating facts about Indian culture and heritage:
        </p>
        """, 
        unsafe_allow_html=True
    )

    # Facts container styling
    for i, item in enumerate(cultural_facts, start=1):
        fact_html = f"""
        <div style='
            background: #e8f0fe;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            font-family: Arial, sans-serif;
            box-shadow: 1px 1px 6px rgba(0,0,0,0.1);
            color: #2c3e50;
        '>
            <h3 style='margin: 0;'>
                {item['icon']} <span style='color: #1a73e8;'>Fact {i}:</span>
            </h3>
            <p style='margin-top: 6px; font-size: 16px;'>{item['fact']}</p>
        </div>
        """
        st.markdown(fact_html, unsafe_allow_html=True)

if __name__ == "__main__":
    show_cultural_facts()
