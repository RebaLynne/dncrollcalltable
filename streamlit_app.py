# Import dependencies
import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# Create a connection object
conn = st.connection("gsheets", type=GSheetsConnection)
google_sheets_table = conn.read()
dataframe = pd.DataFrame(google_sheets_table) # Convert google sheets table into python dataframe. Streamlit expects dataframes as input.

# Introduction text
"""
Hi there! This is a simple Google Sheets example on how to embed a dynamic table on a Medium blog post with Streamlit! 
"""

# Define tabs
tab1, tab2 = st.tabs(["Table", "Graph"])

# Streamlit content
with tab1:
  st.write(dataframe)
with tab2:
  st.line_chart(dataframe,x="Date", y="Close")

