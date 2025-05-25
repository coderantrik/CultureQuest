# utils/snowflake_connection.py

# utils/snowflake_connection.py

import streamlit as st
import snowflake.connector

@st.cache_resource
def create_connection():
    sf_secrets = st.secrets["snowflake"]
    conn = snowflake.connector.connect(
        user=sf_secrets["user"],
        password=sf_secrets["password"],
        account=sf_secrets["account"],
        warehouse=sf_secrets["warehouse"],
        database=sf_secrets["database"],
        schema=sf_secrets["schema"]
    )
    return conn
