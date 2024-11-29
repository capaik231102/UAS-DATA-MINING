import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Load Data
    data = pd.read_csv('data/Data_Tanaman_Padi_Sumatera_version_1.csv')

    st.title("Visualisasi Data")

    # Data Visualization: Produksi Padi Berdasarkan Provinsi
    fig, ax = plt.subplots(figsize=(16, 8))
    sns.barplot(x=data['Provinsi'], y=data['Produksi'], ax=ax, palette='viridis')
    ax.set_title('Produksi Padi Berdasarkan Provinsi di Sumatera', fontsize=16)
    ax.set_xlabel('Provinsi', fontsize=12)
    ax.set_ylabel('Produksi (ton)', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    st.pyplot(fig)
    
    # Visualisasi Produksi Padi Berdasarkan Provinsi
    st.subheader('Produksi Padi Berdasarkan Provinsi di Sumatera')
    st.text("Grafik batang ini menunjukkan produksi padi di berbagai provinsi di Sumatera.")
    st.text("Sumbu vertikal (y) menunjukkan jumlah produksi padi dalam ton.")
    st.text("Sumbu horizontal (x) menunjukkan nama-nama provinsi di Sumatera.")
    st.text("Sumatera Utara memiliki produksi padi tertinggi, diikuti oleh Sumatera Selatan dan Lampung.")
    st.text("Provinsi dengan produksi padi terendah adalah Bengkulu dan Jambi.")

    # Data Visualization: Produksi Padi Berdasarkan Tahun
    fig, ax = plt.subplots(figsize=(16, 8))
    sns.barplot(x='Tahun', y='Produksi', data=data, ax=ax, palette='viridis')
    ax.set_title('Produksi Padi Berdasarkan Tahun di Sumatera', fontsize=16)
    ax.set_xlabel('Tahun', fontsize=12)
    ax.set_ylabel('Produksi (ton)', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    st.pyplot(fig)
    
    # Visualisasi Produksi Padi Berdasarkan Tahun
    st.subheader('Produksi Padi Berdasarkan Tahun')
    st.text("Grafik batang ini menunjukkan produksi padi di Sumatera dari tahun 1998 hingga 2023.")
    st.text("Sumbu vertikal (y) menunjukkan jumlah produksi padi dalam ton.")
    st.text("Sumbu horizontal (x) menunjukkan tahun produksi.")
    st.text("Terlihat tren peningkatan produksi padi dari tahun 1998 hingga mencapai puncaknya sekitar tahun 2017, kemudian mengalami fluktuasi hingga tahun 2020.")

    # Data Visualization: Suhu Rata-rata dan Produksi
    fig, ax = plt.subplots(figsize=(16, 8))
    sns.lineplot(x='Suhu rata-rata', y='Produksi', data=data, ax=ax)
    ax.set_title('Hubungan Suhu Rata-rata dan Produksi Padi', fontsize=16)
    ax.set_xlabel('Suhu Rata-rata', fontsize=12)
    ax.set_ylabel('Produksi (ton)', fontsize=12)
    st.pyplot(fig)
    

    # Visualisasi Hubungan Antara Suhu Rata-rata dan Produksi Padi
    st.subheader('Hubungan Antara Suhu Rata-rata dan Produksi Padi')
    st.text("Grafik menunjukkan bahwa produksi padi bervariasi secara signifikan dengan perubahan suhu rata-rata.")
    st.text("Pada suhu yang lebih rendah (sekitar 22-25 derajat), produksi padi cenderung lebih stabil dan relatif lebih rendah.")
    st.text("Pada suhu yang lebih tinggi (sekitar 26-30 derajat), produksi padi menunjukkan fluktuasi yang lebih besar dan jumlah produksi yang lebih tinggi.")


    # Data Visualization: Perubahan Suhu Rata-rata Berdasarkan Tahun
    fig, ax = plt.subplots(figsize=(16, 8))
    sns.lineplot(x='Tahun', y='Suhu rata-rata', data=data, color='red', ax=ax)
    ax.set_title('Perubahan Suhu Rata-rata Berdasarkan Tahun di Sumatera', fontsize=16)
    ax.set_xlabel('Tahun', fontsize=12)
    ax.set_ylabel('Suhu Rata-rata (°C)', fontsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
    st.pyplot(fig)
    
        # Visualisasi Perubahan Suhu Rata-rata Berdasarkan Tahun di Sumatera
    st.subheader('Perubahan Suhu Rata-rata Berdasarkan Tahun di Sumatera')
    st.text("Grafik ini menunjukkan perubahan suhu rata-rata di Sumatera dari tahun 1995 hingga 2020.")
    st.text("Sumbu horizontal (x) menunjukkan tahun, mulai dari 1995 hingga 2020.")
    st.text("Sumbu vertikal (y) menunjukkan suhu rata-rata dalam derajat Celsius (°C), dengan rentang dari 25°C hingga 30°C.")
    st.text("Grafik garis merah menunjukkan tren suhu rata-rata selama periode ini, dengan area berbayang menunjukkan variasi suhu.")
    st.text("Terdapat fluktuasi signifikan dalam suhu, dengan puncak notable sekitar tahun 2000 dan penurunan tajam sesudahnya.")
    st.text("Suhu cenderung stabil pada beberapa tahun berikutnya namun tetap menunjukkan variasi.")

    # Data Visualization: Curah Hujan dan Produksi
    fig, ax = plt.subplots(figsize=(16, 8))
    sns.lineplot(x='Curah hujan', y='Produksi', data=data, color='green', ax=ax)
    ax.set_title('Hubungan Curah Hujan dan Produksi Padi', fontsize=16)
    ax.set_xlabel('Curah Hujan (mm)', fontsize=12)
    ax.set_ylabel('Produksi (ton)', fontsize=12)
    st.pyplot(fig)
    
    # Visualisasi Hubungan Antara Curah Hujan dan Produksi Padi
    st.subheader('Hubungan Antara Curah Hujan dan Produksi Padi')
    st.text("Grafik ini menunjukkan hubungan antara curah hujan dan produksi padi di Sumatera.")
    st.text("Sumbu horizontal (x) menunjukkan curah hujan dalam milimeter (mm).")
    st.text("Sumbu vertikal (y) menunjukkan produksi padi dalam ton.")
    st.text("Garis hijau yang berfluktuasi menunjukkan jumlah produksi padi pada berbagai tingkat curah hujan.")
    st.text("Dari grafik ini, kita bisa melihat bagaimana perubahan curah hujan mempengaruhi produksi padi.")


    # Data Visualization: Kelembapan dan Produksi
    fig, ax = plt.subplots(figsize=(16, 8))
    sns.lineplot(x='Kelembapan', y='Produksi', data=data, color='m', ax=ax)
    ax.set_title('Hubungan Kelembapan dan Produksi Padi', fontsize=16)
    ax.set_xlabel('Kelembapan (%)', fontsize=12)
    ax.set_ylabel('Produksi (ton)', fontsize=12)
    st.pyplot(fig)

    # Visualisasi Hubungan Antara Kelembapan dan Produksi Padi
    st.subheader('Hubungan Antara Kelembapan dan Produksi Padi')
    st.text("Grafik ini menunjukkan hubungan antara kelembapan dan produksi padi di Sumatera.")
    st.text("Sumbu horizontal (x) menunjukkan kelembapan dalam persentase (%).")
    st.text("Sumbu vertikal (y) menunjukkan produksi padi dalam ton.")
    st.text("Garis ungu yang berfluktuasi menunjukkan jumlah produksi padi pada berbagai tingkat kelembapan.")
    st.text("Grafik ini membantu kita memahami bagaimana variasi kelembapan dapat mempengaruhi produksi padi.")
