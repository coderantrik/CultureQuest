# utils/snowflake_connection.py

import streamlit as st
import snowflake.connector

@st.cache_resource
def create_connection():
    sf_secrets = st.secrets["snowflake"]
    conn = snowflake.connector.connect(
        user=sf_secrets["ANTRIK09"],
        password=sf_secrets["Akshansh@7523869509"],
        account=sf_secrets["HJKVCXU-UP61395"],
        warehouse=sf_secrets["COMPUTE_WH"],
        database=sf_secrets["CULTUREQUEST_DB"],
        schema=sf_secrets["PUBLIC"]
    )
    return conn
