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

st.header('Posljednji rezultati')

#def rezultat_matcha(id):

for index, row in last_matches.iterrows():
    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,3])
    with col1:
        st.write(str(row['Datum_meča']))
    with col2:
        st.markdown('<h5 style="color: '+str(row['Protivnik_1_boja'])+'">'+str(row['Protivnik_1'])+'</h5>', unsafe_allow_html=True)
    with col3:
        st.markdown('<h5>'+str(row['Rezultat_1'])+' : '+str(row['Rezultat_2'])+'</h5>', unsafe_allow_html=True)
    with col4:
        st.markdown('<h5 style="color: '+str(row['Protivnik_2_boja'])+'">'+str(row['Protivnik_2'])+'</h5>', unsafe_allow_html=True)



igraci = pd.read_excel('table_tennis.xlsx', sheet_name='Osobe')
igraci = igraci.sort_values(by=['Rang'], ascending=True)


st.header('Tabela igrača')
st.write(igraci)

for index, row in igraci.iterrows():
    col1, col2, col3, col4, col5 = st.columns([1,1,1,1,3])
    with col1:
        st.write(row['Rang'])

st.header('Statistike igrača')
igrac = st.selectbox(label='Igrač', options=igraci)
