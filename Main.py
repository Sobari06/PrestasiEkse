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
            page_title="Gantari Prestasi",
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

dfh= pd.read_excel(
    io='PrestasiEkse.xlsx',
    engine='openpyxl',
    sheet_name='Table',
    usecols=[1,2,3,4,5,6,7,8,9,10,11,12])
dfh = dfh.set_index(pd.Index(range(1, len(dfh) + 1)))

print(dfh)



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
url = "https://assets8.lottiefiles.com/packages/lf20_sy6mqjxk.json"


# Menampilkan animasi Lottie di tampilan utama Streamlit
st_lottie(load_lottie_url(url))

col1, col2= st.columns([2,1])
with col1:
            st.title('Dashboard Prestasi Mahasiswa PKU IPB Angkatan 59')
            st.subheader("Ormawa Eksekutif PKU IPB Kabinet Gantari Arti")   
with col2:
        # Tampilkan informasi nilai mutu
             st.image('RISBANG X AKPRES.png', width=300)

st.markdown('-------------') 
st.write("Dashboard Prestasi Mahasiswa PKU IPB Angkatan 59 ini bertujuan untuk memberikan pemahaman yang lebih baik tentang pencapaian akademik dan non-akademik mahasiswa PKU IPB, serta mengapresiasi prestasi yang telah mereka raih. Dengan adanya dashboard ini, diharapkan dapat memberikan informasi terkait perkembangan prestasi mahasiswa, sehingga dapat memberikan motivasi dan inspirasi dalam mengejar prestasi lebih baik.")
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

#=============================== Data Foto ===========================================

Add = "Add.png"
fag1 = "Syafira Tiara Pungkii.png"

#=============================== FAPERTA ===========================================
fagA1 ="IrziFinal(A).png"
fagA2="Irzi2(A).png"
fagA3 ="Diaz(A).png"
#=============================== SKHB ===========================================
fagB1 ="Nadelia(B).png"
#=============================== FPIK ===========================================
fagC1 ="FahmiFinal(C).png"
fagC2="Alfaroby(C).png"
fagC3 ="Fahmi(C) (2).png"
#=============================== FAPET ===========================================

fagD1 ="Taufiq(D).png"
#=============================== FAHUTAN ===========================================
fagE1 ="Syafira Tiara Pungkii.png"
fagE2 ="Akbar(E).png"
fagE3 ="Aditya(E).png"
fagE4 ="Achmad(E).png"

#=============================== FATETA ===========================================
fagF1 =""
#=============================== FMIPA ===========================================
fagG1 ="AhmadFinal(G).png"
fagG2 ="Haidar(G) (2).png"
fagG3 ="Haidar(G).png"
fagG4 ="RafiFinal(G).png"
fagG5 ="Rafi2(G).png"
fagG6 ="Rafi3(G).png"
fagG7 ="Rafi4(G).png"
#=============================== FEM ===========================================
fagH1 ="Abdul(H).png"
fagH2 ="Hamidatul(H).png"
fagH3 ="Regita(H).png"
fagH4 ="YudaFinal(H).png"
fagH5 ="Rifdah(H).png"
fagH6 = "Ali(H).png"
fagH7 ="Ali(H).png"

#=============================== FEMA ===========================================
fagI1 ="Amrul(I).png"
#=============================== SB ===========================================
fag21 =""
fag22 =""
fag23 =""
fag24 =""
fag25 =""
fag26 =""
fag27 =""

# Membuat FIltrasi menggunakan Selectbox

st.subheader("Filtrasi Prestasi Mahasiswa FAPERTA PKU IPB Angkatan 59 Berdasarkan Fakultas")
menu = ["FAPERTA","SKHB", "FPIK","FAPET","FAHUTAN","FATETA","FMIPA", "FEM", "FEMA","SB" ]
selected_menu = st.selectbox("Fakultas", menu) 


if selected_menu == "FAPERTA":

#=============================== FAPERTA ===========================================
    st.markdown('-------------')
    st.subheader('Prestasi Mahasiswa FAPERTA PKU IPB Angkatan 59')
    left_column, middle_column, right_column, add= st.columns([4, 4, 4, 4])
    left_column.image(fagA1, use_column_width=True)
    middle_column.image(fagA3, use_column_width=True)
    right_column.image(Add, use_column_width=True)
    add.image(Add, use_column_width=True)

elif selected_menu == "FATETA":
#=============================== FATETA ===========================================
    st.markdown('-------------')
    st.subheader('Prestasi Mahasiswa FATETA PKU IPB Angkatan 59')

    left_column, middle_column, right_column, add= st.columns([4, 4, 4, 4])
    left_column.image(Add, use_column_width=True)
    middle_column.image(Add, use_column_width=True)
    right_column.image(Add, use_column_width=True)
    add.image(Add, use_column_width=True)

elif selected_menu == "FPIK":

#=============================== FPIK ===========================================
    st.markdown('-------------')
    st.subheader('Prestasi Mahasiswa FPIK PKU IPB Angkatan 59')

    left_column, middle_column, right_column, add= st.columns([4, 4, 4, 4])
    left_column.image(fagC1, use_column_width=True)
    middle_column.image(fagC2, use_column_width=True)
    right_column.image(Add, use_column_width=True)
    add.image(Add, use_column_width=True)

elif selected_menu == "FEMA":
#=============================== FEMA ===========================================
    st.markdown('-------------')
    st.subheader('Prestasi Mahasiswa FEMA PKU IPB Angkatan 59')

    left_column, middle_column, right_column, add= st.columns([4, 4, 4, 4])
    left_column.image(fagI1, use_column_width=True)
    middle_column.image(Add, use_column_width=True)
    right_column.image(Add, use_column_width=True)
    add.image(Add, use_column_width=True)

elif selected_menu == "SKHB":
#=============================== SKHB ===========================================
    st.markdown('-------------')
    st.subheader('Prestasi Mahasiswa SKHB PKU IPB Angkatan 59')

    left_column, middle_column, right_column, add= st.columns([4, 4, 4, 4])
    left_column.image(fagB1, use_column_width=True)
    middle_column.image(Add, use_column_width=True)
    right_column.image(Add, use_column_width=True)
    add.image(Add, use_column_width=True)
elif selected_menu == "FMIPA":
#=============================== FMIPA ===========================================
    st.markdown('-------------')
    st.subheader('Prestasi Mahasiswa FMIPA PKU IPB Angkatan 59')

    left_column, middle_column, right_column, add= st.columns([4, 4, 4, 4])
    left_column.image(fagG1, use_column_width=True)
    middle_column.image(fagG3, use_column_width=True)
    right_column.image(fagG4, use_column_width=True)
    add.image(Add, use_column_width=True)

    left_column, middle_column, right_column, add= st.columns([4, 4, 4, 4])
    left_column.image(Add, use_column_width=True)
    middle_column.image(Add, use_column_width=True)
    right_column.image(Add, use_column_width=True)
    add.image(Add, use_column_width=True)

elif selected_menu == "SB":
#=============================== SB ===========================================
    st.markdown('-------------')
    st.subheader('Prestasi Mahasiswa SB PKU IPB Angkatan 59')

    left_column, middle_column, right_column, add= st.columns([4, 4, 4, 4])
    left_column.image(Add, use_column_width=True)
    middle_column.image(Add, use_column_width=True)
    right_column.image(Add, use_column_width=True)
    add.image(Add, use_column_width=True)

elif selected_menu == "FAPET":
#=============================== FAPET ===========================================
    st.markdown('-------------')
    st.subheader('Prestasi Mahasiswa FAPET PKU IPB Angkatan 59')

    left_column, middle_column, right_column, add= st.columns([4, 4, 4, 4])
    left_column.image(fagD1, use_column_width=True)
    middle_column.image(Add, use_column_width=True)
    right_column.image(Add, use_column_width=True)
    add.image(Add, use_column_width=True)

elif selected_menu == "FAHUTAN":
#=============================== FAHUTAN ===========================================
    st.markdown('-------------')
    st.subheader('Prestasi Mahasiswa FAHUTAN PKU IPB Angkatan 59')

    left_column, middle_column, right_column, add= st.columns([4, 4, 4, 4])
    left_column.image(fagE1, use_column_width=True)
    middle_column.image(fagE2, use_column_width=True)
    right_column.image(fagE3, use_column_width=True)
    add.image(fagE4, use_column_width=True)

elif selected_menu == "FEM":
#=============================== FEM ===========================================
    st.markdown('-------------')
    st.subheader('Prestasi Mahasiswa FEM PKU IPB Angkatan 59')

    left_column, middle_column, right_column, add= st.columns([4, 4, 4, 4])
    left_column.image(fagH1, use_column_width=True)
    middle_column.image(fagH2, use_column_width=True)
    right_column.image(fagH3, use_column_width=True)
    add.image(fagH4, use_column_width=True)

    left_column, middle_column, right_column, add= st.columns([4, 4, 4, 4])
    left_column.image(fagH5, use_column_width=True)
    middle_column.image(fagH6, use_column_width=True)
    right_column.image(Add, use_column_width=True)
    add.image(Add, use_column_width=True)

st.markdown('-------------')
st.subheader('Dataframe Prestasi Mahasiswa PKU IPB Angkatan 59')
st.write('Terdapat sistem filtrasi data yang bisa membantu anda untuk mencari data dengan lebih cepat')

# Menambahkan filter
filter_options = {
    'Fakultas': dfh['Fakultas'].unique(),
    'Jenis Prestasi': dfh['Jenis Prestasi'].unique(),
    'Skala Lomba/Pertandingan': dfh['Skala Lomba/Pertandingan'].unique(),
}

selected_filters = {}

for option, values in filter_options.items():
    selected_filters[option] = st.multiselect(f"Pilih {option}", values)

# Memfilter data berdasarkan filter yang dipilih
filtered_df = dfh.copy()

for option, selected_values in selected_filters.items():
    if selected_values:
        filtered_df = filtered_df[filtered_df[option].isin(selected_values)]

# Menampilkan data yang terfilter
st.write("Data Terfilter:")
st.write(filtered_df)



