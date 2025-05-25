# 🎨 CultureQuest 🇮🇳

**CultureQuest** is an interactive Streamlit web application that celebrates the rich cultural heritage of India. It allows users to explore hidden cultural gems, visualize tourism trends, discover diverse art forms, and embrace sustainable travel—all through an engaging, data-first experience.

---

## 🌐 Live App

🔗 [Visit CultureQuest](culturequest-yvkx3wsya9bqjsmrybiwpm.streamlit.app)

---

## 📌 Features

- 🧭 **Home**: Overview and mission of CultureQuest.
- 🏔 **Hidden Gems**: Discover offbeat locations rich in history and tradition.
- 📈 **Tourism Trends**: Visual analytics of tourism data across Indian states.
- 📚 **Cultural Facts**: Bite-sized cultural insights and stories.
- 🌿 **Travel Tips**: Sustainable travel suggestions for eco-conscious journeys.

---

## 🧰 Tech Stack

| Tool | Usage |
|------|-------|
| [Streamlit](https://streamlit.io/) | Web App Framework |
| [Snowflake](https://www.snowflake.com/) | Cloud Data Warehouse |
| [Altair](https://altair-viz.github.io/) | Declarative Data Visualization |
| [PyDeck](https://deckgl.readthedocs.io/) | 3D Geospatial Maps |
| [Pandas](https://pandas.pydata.org/) | Data Handling |
| [Matplotlib](https://matplotlib.org/) | Required for Data Styling |
| [Lottie](https://lottiefiles.com/) | Animations |
| [GitHub](https://github.com/) | Version Control & Collaboration |

---

## 🏗 Folder Structure

├── Home.py
├── pages/
│ ├── 1_HiddenGems.py
│ ├── 2_Trends.py
│ ├── 3_Cultural_Facts.py
│ └── 4_TravelTips.py
├── utils/
│ ├── snowflake_connection.py
│ └── ui_helpers.py
├── data/
│ └── (CSV, JSON files used)
├── requirements.txt
└── README.md

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/coderantrik/culturequest.git
cd culturequest

1.1Create and Activate Virtual Environment:

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

1.2 Install Dependencies:

pip install -r requirements.txt

1.3  Run the App

streamlit run Home.py

📊 Example Visuals:
Heatmaps of top tourist states

Altair bar charts for trend comparisons

Interactive maps using PyDeck

✨ Contributing
We welcome contributions! Please fork the repo, create a new branch, and submit a pull request.

🛡 License
This project is licensed under the MIT License.

💡 Inspiration
Built with love to promote cultural literacy, data-driven storytelling, and sustainable travel for the world’s most diverse country. 🌺


---

Would you like a badge section (e.g., Streamlit Cloud status, GitHub stars) or a shorter version for portfolio use?


