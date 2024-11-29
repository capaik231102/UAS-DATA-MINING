import streamlit as st
import pandas as pd

def main():
    # Load Data
    data = pd.read_csv('data/Data_Tanaman_Padi_Sumatera_version_1.csv')

    # Display Data
    st.title("Data Awal")
    st.write(data)
    st.write("Data diatas merupakan data awal yang akan saya olah yaitu data produksi padi di Pulau Sumatera dari tahun 1993-2020")

    # Data Overview
    st.write("Deskripsi Data")
    st.write(data.describe())
    st.text("Tabel ini merangkum statistik deskriptif untuk enam variabel: Tahun, Produksi, Luas Panen, Curah Hujan, Kelembapan, dan Suhu Rata-rata. Statistik deskriptif ini memberikan gambaran umum tentang distribusi data untuk setiap variabel.")

    # Missing Values
    st.write("Missing Values")
    st.write(data.isnull().sum())
    st.text("Ini merupakan pengecekan nilai hilang pada data diatas")
    