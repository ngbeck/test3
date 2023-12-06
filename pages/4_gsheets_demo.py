import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1lwRc-ftgk00ZcN-ARh2rpm0fX8x991aAwwNa-qvUddI/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

#add nrows to manage rows and usecols to manage columns
data = conn.read(spreadsheet=url)
st.dataframe(data)