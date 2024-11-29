import streamlit as st

def main():
    st.title("Prediksi Swasembada Pangan (Padi) di Pulau Sumatera")
    
    st.header("TUGAS UAS DATA MINING - FAIRUZ ZAIN NIT 22191090")
    
    st.write("""
    Selamat datang di aplikasi prediksi swasembada pangan di Pulau Sumatera. Aplikasi ini dirancang untuk membantu pengambilan keputusan 
    dengan memberikan prediksi produksi padi menggunakan model machine learning. Berikut adalah gambaran singkat mengenai aplikasi ini:

    ### Latar Belakang
    Pertanian adalah salah satu sektor vital yang menunjang perekonomian Indonesia, terutama di Pulau Sumatera. Dengan semakin meningkatnya 
    kebutuhan pangan, penting bagi kita untuk memiliki alat yang mampu memprediksi hasil panen dengan akurasi yang tinggi. 
    Melalui aplikasi ini, data historis dan kondisi cuaca dianalisis untuk memberikan prediksi yang dapat diandalkan.

    ### Tujuan
    1. Memberikan prediksi produksi padi yang akurat di Pulau Sumatera.
    2. Membantu pengambil kebijakan dalam perencanaan dan strategi ketahanan pangan.
    3. Menggunakan model machine learning untuk memproses data dengan lebih efisien.

    ### Data yang Digunakan
    Data yang digunakan dalam aplikasi ini mencakup berbagai faktor yang mempengaruhi produksi padi, antara lain:
    1. **Provinsi**: Lokasi geografis di Sumatera.
    2. **Tahun**: Tahun pengumpulan data.
    3. **Luas Panen**: Luas lahan yang digunakan untuk menanam padi (dalam hektar).
    4. **Produksi**: Jumlah padi yang dihasilkan (dalam ton).
    5. **Suhu Rata-rata**: Suhu rata-rata tahunan (dalam derajat Celsius).
    6. **Curah Hujan**: Jumlah curah hujan tahunan (dalam milimeter).
    7. **Kelembapan**: Tingkat kelembapan rata-rata (dalam persen).

    ### Proses dan Metodologi
    1. **Pengumpulan Data**: Data diperoleh dari sumber-sumber terpercaya yang mencakup data historis produksi padi dan faktor-faktor cuaca.
    2. **Pra-Pemrosesan Data**: Data diolah untuk menghilangkan nilai yang hilang, melakukan encoding pada variabel kategorikal, dan melakukan scaling pada fitur numerik.
    3. **Analisis Eksploratif Data (EDA)**: Data divisualisasikan untuk memahami distribusi dan pola.
    4. **Pemodelan Machine Learning**: Model dibangun menggunakan algoritma seperti Linear Regression, Random Forest Regressor, dan Decision Tree Regressor.
    5. **Evaluasi Model**: Model dievaluasi menggunakan metrik seperti Mean Squared Error (MSE), Mean Absolute Error (MAE), dan R-squared.
    6. **Prediksi dan Interpretasi**: Model yang sudah dilatih digunakan untuk memprediksi produksi padi dan hasilnya divisualisasikan.

    ### Halaman Aplikasi
    1. **Home**: Halaman ini berisi pengenalan diri, alasan mengerjakan proyek ini, dan gambaran umum aplikasi.
    2. **Pengolah Data**: Menampilkan proses pra-pemrosesan data dan analisis deskriptif.
    3. **Visualisasi**: Menampilkan berbagai visualisasi data yang memberikan insight tentang produksi padi di Sumatera.
    4. **Pemodelan**: Menampilkan proses pembuatan dan evaluasi model machine learning.
    5. **Evaluasi Model**: Menampilkan proses evaluasi dari data yang sudah diolah.
    6. **Kesimpulan**: Menampilkan kesimpulan dari hasil analisis dan ucapan terima kasih.
    """)

  