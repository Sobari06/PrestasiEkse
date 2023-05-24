import streamlit as st
import pandas as pd
import plotly_express as px
import openpyxl as ox
from PIL import Image


dfa= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(Fakultas)',
    usecols='A:B')
names = dfa['Fakultas'].apply(str)
values = dfa['Count'].apply(int)

fig1= px.histogram(
dfa, x= values,  
title= 'Berdasarkan Fakultas')
print(dfa)

dfb= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(Jenis Kelamin)',
    usecols='A:B')
names = dfb['JenisKelamin'].apply(str)
values = dfb['Count'].apply(int)

fig2= px.pie(dfb, values= values, 
names= names, 
title= 'Berdasarkan Jenis Kelamin')
print(dfb)

dfc= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(JenisPrestasi)',
    usecols='A:B')
names = dfc['JenisPrestasi'].apply(str)
values = dfc['Count'].apply(int)

fig3= px.histogram(dfc, x= values, 
title= 'Berdasarkan Jenis Prestasi')
print(dfc)

dfd= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(Bulan)',
    usecols='A:B')
names = dfd['Bulan'].apply(str)
values = dfd['Count'].apply(int)

fig4= px.line(dfd, y= values, 
x= names, 
title= 'Berdasarkan Bulan')
print(dfd)

dfe= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(SkalaLomba)',
    usecols='A:B')
names = dfe['SkalaLomba'].apply(str)
values = dfe['Count'].apply(int)

fig5= px.histogram(dfe, x= values, 
title= 'Berdasarkan Skala Lomba')
print(dfe)

dff= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(PelaksanaanLomba)',
    usecols='A:B')
names = dff['PelaksanaanLomba'].apply(str)
values = dff['Count'].apply(int)

fig6= px.pie(dff, values= values, 
names= names, 
title= 'Berdasarkan Jenis Perlombaan')
print(dff)

#Visualisasi Grafik Prestasi Eksekutif Ormawa
st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
st.plotly_chart(fig4)
st.plotly_chart(fig5)
st.plotly_chart(fig6)
