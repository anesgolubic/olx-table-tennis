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
matches = matches.sort_values(by=['Datum_meča','ID'], ascending=False)
last_matches = matches[0:10]

st.write('Posljednji rezultati')
st.write(last_matches)

#def rezultat_matcha(id):

for index, row in last_matches.iterrows():
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.write(str(row['Datum_meča']))
    with col2:
        st.markdown('<h5>'+str(row['Protivnik_1'])+'</h5>', unsafe_allow_html=True)
    with col3:
        st.markdown('<h4>'+str(row['Rezultat_1'])+' : '+str(row['Rezultat_2'])+'</h4>', unsafe_allow_html=True)
    with col4:
        st.markdown('<h5>'+str(row['Protivnik_2'])+'</h5>', unsafe_allow_html=True)
    st.divider()

for index, row in last_matches.iterrows():
    st.markdown('<h5>'+str(row['Protivnik_1'])+'</h5><h4>'+str(row['Rezultat_1'])+' : '+str(row['Rezultat_2'])+'</h4><h5>'+str(row['Protivnik_2'])+'</h5>', unsafe_allow_html=True)