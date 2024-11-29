import streamlit as st

# Menambahkan navigasi halaman
st.sidebar.title("Analisis Swasembada Pangan (PADI)")
page = st.sidebar.selectbox("Pilih Halaman", ["Home", "Pengolah Data", "Visualisasi", "Pemodelan","Evaluasi Model","Kesimpulan"])

if page == "Home":
    import home
    home.main()
elif page == "Pengolah Data":
    import data_processing
    data_processing.main()
elif page == "Visualisasi":
    import visualization
    visualization.main()
elif page == "Pemodelan":
    import model_training
    model_training.main()
elif page == "Evaluasi Model":
    import model_evaluation
    model_evaluation.main()     
elif page == "Kesimpulan":
    import conclusion
    conclusion.main()
