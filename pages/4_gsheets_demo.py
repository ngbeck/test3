import streamlit as st
from streamlit_gsheets import GSheetsConnection

url = "https://docs.google.com/spreadsheets/d/1lwRc-ftgk00ZcN-ARh2rpm0fX8x991aAwwNa-qvUddI/edit?usp=sharing"

conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read(
    worksheet="Oilers Influence 18-19",
    ttl="10m",
    nrows=3,
)

for row in df.intertuples():
    st.write(f"{row.name} has a :{row.pet}:")