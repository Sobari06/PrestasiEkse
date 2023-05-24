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

fig1= px.bar(
dfa, y= values,  x=names,
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

fig3= px.bar(dfc, y= values, x=names,
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

fig5= px.bar(dfe, x= values, y=names,
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

#=============================== BEST PERFORMANCE BPH SEBAGAI SC ===========================================
st.title('Advocare Introduction')

st.write("Advocare menyelesaikan setiap masalah dengan cepat dan tepat. Kami fokus pada kepuasan dan kesejahteraan Anda, dan menawarkan layanan profesional dan responsif. Kami terlatih menangani segala jenis keluhan dan berkomitmen memberikan solusi memuaskan. Dengan Advocare, Anda tenang dan terjamin masalah Anda ditangani dengan keahlian yang sesuai.")
#=============================== Skala Lomba ===========================================
st.markdown('-------------')   
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Jumlah Prestasi", 27)
with col2:
    st.metric("Internasional", 2)
with col3:
    st.metric("Nasional", 20)
with col4:
    st.metric("Regional", 5)
st.markdown('-------------')

#=============================== Bulan ===========================================
st.plotly_chart(fig4)
st.markdown('-------------')

#=============================== Jenis Perlombaan ===========================================
#=============================== Jenis Kelamin ===========================================
left_column, Right_Column = st.columns([4,4])
left_column.plotly_chart(fig6, use_container_width=True)
Right_Column.plotly_chart(fig2,use_container_width=True)
st.markdown('-------------')

#=============================== Fakultas ===========================================
#=============================== Jenis Prestasi ===========================================

left_column, Right_Column = st.columns([4,4])
left_column.plotly_chart(fig1, use_container_width=True)
Right_Column.plotly_chart(fig3,use_container_width=True)

# st.markdown('-------------')
# st.plotly_chart(fig1)
# st.markdown('-------------')


# st.plotly_chart(fig3)
# st.markdown('-------------')



#=============================== Skala Lomba ===========================================
# st.plotly_chart(fig5)
# st.markdown('-------------')

