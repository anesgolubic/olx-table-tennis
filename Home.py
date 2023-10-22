import streamlit as st
st.set_page_config(
    page_title="OLX.ba Table Tennis Liga",
    #page_icon="🧊",
    layout="wide",
)

import pandas as pd
from datetime import date
from datetime import date, timedelta

# LINK TO THE CSS FILE
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

"""
# OLX.ba Table Tennis Liga
"""

matches = pd.read_excel('table_tennis.xlsx', sheet_name='Matchevi')
matches['Datum_meča'] = matches['Datum_meča'].dt.date
matches = matches.sort_values('Datum_meča', inplace=True)
#last_matches = matches[0:10]

st.write('Posljednji rezultati')
st.write(matches)