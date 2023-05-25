import streamlit as st
import pandas as pd
import plotly_express as px
import openpyxl as ox
from PIL import Image
from streamlit_lottie import st_lottie
import requests

# Mengatur konfigurasi tampilan Streamlit
def set_page_config():
        st.set_page_config(
            page_title="Dashboard Prestasi Mahasiswa PKU IPB 59",
            page_icon='LOGO EKSE1.png',
            layout="wide",
            initial_sidebar_state="expanded",
        )

# Memanggil fungsi set_page_config()
set_page_config()


dfa= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(Fakultas)',
    usecols='A:B')
names = dfa['Fakultas'].apply(str)
values = dfa['Count'].apply(int)

fig1= px.bar(
dfa, y= values,  x=names,
title= 'Fakultas')
print(dfa)
fig1.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )

dfb= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(Jenis Kelamin)',
    usecols='A:B')
names = dfb['JenisKelamin'].apply(str)
values = dfb['Count'].apply(int)

fig2= px.pie(dfb, values= values, 
names= names, 
title= 'Jenis Kelamin')
print(dfb)

dfc= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(JenisPrestasi)',
    usecols='A:B')
names = dfc['JenisPrestasi'].apply(str)
values = dfc['Count'].apply(int)

fig3= px.bar(dfc, y= values, x=names,
title= 'Jenis Prestasi')
print(dfc)
fig3.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )

dfd= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(Bulan)',
    usecols='A:B')
names = dfd['Bulan'].apply(str)
values = dfd['Count'].apply(int)

fig4= px.line(dfd, y= values, 
x= names, 
title= 'Jumlah Prestasi Berdasarkan Bulan')
print(dfd)
fig4.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )

dfe= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(SkalaLomba)',
    usecols='A:B')
names = dfe['SkalaLomba'].apply(str)
values = dfe['Count'].apply(int)

fig5= px.bar(dfe, x= values, y=names,
title= 'Jumlah Prestasi Berdasarkan Skala Lomba')
print(dfe)
fig5.update_layout(
            dragmode="pan",
            hovermode="x",
            autosize=True
        )

dff= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(PelaksanaanLomba)',
    usecols='A:B')
names = dff['PelaksanaanLomba'].apply(str)
values = dff['Count'].apply(int)

fig6= px.pie(dff, values= values, 
names= names, 
title= 'Jenis Perlombaan')
print(dff)

dfg= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='GX(KategoriPrestasi)',
    usecols='A:B')
names = dfg['KategoriPrestasi'].apply(str)
values = dfg['Count'].apply(int)

fig7= px.pie(dfg, values= values, 
names= names, 
title= 'Kategori Prestasi')
print(dfg)

#Visualisasi Grafik Prestasi Eksekutif Ormawa
#Mendefinisikan fungsi untuk menampilkan animasi Lottie
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Mendefinisikan URL animasi Lottie yang akan ditampilkan
url = "https://assets2.lottiefiles.com/packages/lf20_apg1cx0v.json"


# Menampilkan animasi Lottie di tampilan utama Streamlit
st_lottie(load_lottie_url(url))

col1, col2= st.columns([2,1])
with col1:
            st.title('Dashboard Prestasi Mahasiswa PKU IPB Angkatan 59')
            st.subheader("Ormawa Eksekutif PKU IPB Kabinet Gantari Arti")   
with col2:
        # Tampilkan informasi nilai mutu
             st.image('RISBANG X INTERNAL.png', width=300)

st.markdown('-------------') 
st.write("Dashboard Prestasi Mahasiswa PKU IPB Angkatan 59 ini bertujuan untuk memberikan pemahaman yang lebih baik tentang pencapaian akademik dan non-akademik mahasiswa PKU IPB, serta mengapresiasi prestasi yang telah mereka raih. Dengan adanya dashboard ini, diharapkan dapat memberikan informasi terkait perkembangan prestasi mahasiswa secara real-time, sehingga dapat memberikan motivasi dan inspirasi dalam mengejar prestasi lebih baik.")
#=============================== Skala Lomba ===========================================
st.markdown('-------------')   
st.subheader('Metriks Prestasi Mahasiswa PKU IPB Angkatan 59')
st.write('Berikut adalah metriks terkait total prestasi yang diperoleh dan jumlah prestasi berdasarkan skala lomba.')

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
st.subheader('Line Chart Prestasi Mahasiswa PKU IPB Angkatan 59')
st.plotly_chart(fig4)
st.markdown('-------------')

#=============================== Jenis Perlombaan ===========================================
#=============================== Jenis Kelamin ===========================================
st.subheader('Pie Chart Prestasi Mahasiswa PKU IPB Angkatan 59')
st.write('Berikut adalah tiga pie chart terkait jumlah prestasi mahasiswa berdasarkan jenis perlombaan, kategori prestasi, dan jenis kelamin.')
left_column,middle_column, Right_Column = st.columns([4,4,4])
left_column.plotly_chart(fig6, use_container_width=True)
middle_column.plotly_chart(fig7,use_container_width=True)
Right_Column.plotly_chart(fig2,use_container_width=True)
st.markdown('-------------')

#=============================== Fakultas ===========================================
#=============================== Jenis Prestasi ===========================================
st.subheader('Bar Chart Prestasi Mahasiswa PKU IPB Angkatan 59')
st.write('Berikut adalah dua bar chart terkait jumlah prestasi mahasiswa berdasarkan fakultas, dan jenis prestasi.')

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

