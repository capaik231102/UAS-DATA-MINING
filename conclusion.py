import streamlit as st

def main():
    st.title("Kesimpulan")
    
    st.write("## Ucapan Terima Kasih")
    st.write("""
    Saya ingin mengucapkan terima kasih yang sebesar-besarnya kepada dosen Analisis Big Data dan Data Mining yang telah memberikan pelajaran yang berharga ini
    """)

    st.write("## Kesimpulan")
    st.write("""
    Proyek ini bertujuan untuk mengembangkan model prediksi produksi padi di Pulau Sumatera dengan menggunakan teknik machine learning. Dalam proyek ini, saya mengumpulkan data historis produksi padi, termasuk berbagai faktor yang mempengaruhi seperti luas panen, suhu rata-rata, curah hujan, dan kelembapan.

    Melalui analisis data yang komprehensif dan pemodelan machine learning, saya berhasil mengidentifikasi model **Linear Regression** sebagai model terbaik untuk prediksi produksi padi. Model ini menunjukkan keseimbangan terbaik antara akurasi prediksi dan stabilitas, dengan nilai Train Score sebesar 85.86%, Test Score sebesar 88.54%, dan nilai Mean Squared Error (MSE) terendah sebesar 143,534,153,105.49.

    Hasil ini menunjukkan bahwa model machine learning dapat memberikan wawasan berharga yang dapat digunakan untuk membantu pengambil keputusan dalam merencanakan strategi produksi padi yang lebih baik. Prediksi yang akurat dapat membantu dalam menentukan waktu tanam yang optimal, alokasi sumber daya yang efisien, dan distribusi hasil panen yang lebih efektif.
    """)

    st.write("## Tantangan dan Peluang")
    st.write("""
    Selama proyek ini, saya menghadapi beberapa tantangan seperti overfitting pada model **Decision Tree Regressor** dan **Random Forest Regressor**. Namun, dengan melakukan tuning parameter dan memilih model yang tepat, saya berhasil mengatasi tantangan tersebut.

    Selain itu, proyek ini membuka peluang untuk pengembangan lebih lanjut, termasuk:
    - **Peningkatan Data**: Mengumpulkan data yang lebih banyak dan lebih beragam untuk meningkatkan akurasi model.
    - **Penggunaan Algoritma Lainnya**: Menerapkan dan menguji algoritma machine learning lainnya untuk mencari model yang mungkin lebih baik.
    - **Ekspansi Prediksi**: Memperluas aplikasi ini untuk mencakup prediksi produksi komoditas pertanian lainnya, seperti jagung dan kedelai.
    """)

    st.write("## Rekomendasi")
    st.write("""
    Berdasarkan hasil analisis dan pemodelan, saya merekomendasikan beberapa langkah untuk meningkatkan produksi padi di Pulau Sumatera:
    1. **Adopsi Model Linear Regression**: Gunakan model ini sebagai alat utama untuk prediksi produksi padi karena terbukti memberikan hasil yang paling akurat dan stabil.
    2. **Pengumpulan Data yang Berkelanjutan**: Terus memperbarui dan memperbanyak data yang digunakan dalam model prediksi untuk menjaga akurasi dan relevansi.
    3. **Peningkatan Infrastruktur Data**: Investasi dalam infrastruktur pengumpulan dan penyimpanan data yang lebih baik untuk mendukung analisis data yang lebih akurat.
    4. **Pelatihan Sumber Daya Manusia**: Memberikan pelatihan kepada staf untuk memahami dan mengelola model prediksi, serta untuk memanfaatkan hasil prediksi dalam pengambilan keputusan.
    5. **Kerjasama dengan Institusi Penelitian**: Bekerja sama dengan institusi penelitian dan akademis untuk mendapatkan wawasan dan metodologi terbaru dalam analisis data dan prediksi produksi.
    6. **Penerapan Teknologi Pertanian Pintar**: Manfaatkan teknologi pertanian pintar seperti sistem irigasi otomatis, drone untuk pemantauan tanaman, dan aplikasi mobile untuk petani guna meningkatkan produktivitas dan efisiensi.
    7. **Pemantauan dan Evaluasi Berkala**: Lakukan monitoring dan evaluasi berkala terhadap performa model untuk memastikan model tetap akurat dan relevan.

    Dengan mengikuti rekomendasi ini, diharapkan produksi padi dapat ditingkatkan secara signifikan, yang pada akhirnya akan meningkatkan ketahanan pangan dan kesejahteraan petani.
    """)

    st.write("## Langkah Selanjutnya")
    st.write("""
    Untuk pengembangan lebih lanjut, model dapat ditingkatkan dengan menambahkan lebih banyak data dan menggunakan algoritma machine learning lainnya. Selain itu, aplikasi ini dapat diperluas untuk mencakup prediksi untuk komoditas lainnya seperti jagung, kedelai, dan tebu. Implementasi model prediksi ini diharapkan dapat membantu dalam merencanakan strategi pertanian yang lebih efektif dan efisien, serta dalam mengambil keputusan yang lebih baik untuk mendukung ketahanan pangan di Indonesia.
    """)

if __name__ == "__main__":
    main()
