import streamlit as st
import gspread
from streamlit_gsheets import GSheetsConnection

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

df = conn.read(spreasheet="https://docs.google.com/spreadsheets/d/1lwRc-ftgk00ZcN-ARh2rpm0fX8x991aAwwNa-qvUddI/edit?usp=sharing")
st.dataframe(df)
