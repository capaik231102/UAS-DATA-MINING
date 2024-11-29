import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score

def main():
    # Load Data
    data = pd.read_csv('data/Data_Tanaman_Padi_Sumatera_version_1.csv')

    # Data Preparation
    df = data.copy()
    df['Provinsi'] = df['Provinsi'].astype('category')
    numeric_cols = [col for col in df.columns if df[col].dtype != 'object' and df[col].dtype.name != 'category']
    df_numeric = df[numeric_cols]

    # One Hot Encoding
    string_feat = ['Provinsi']
    ohe = OneHotEncoder()
    ohe.fit(df[string_feat])
    data_ohe_res = pd.DataFrame(ohe.transform(df[string_feat]).toarray(), columns=ohe.get_feature_names_out())
    df = pd.concat([df, data_ohe_res], axis=1)
    df = df.drop(columns=string_feat)

    # Drop 'Tahun'
    df = df.drop(columns='Tahun')

    # Split Data
    x = df.drop('Produksi', axis=1)
    y = df[['Produksi']]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

    # Standardization
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)
    y_train = sc.fit_transform(y_train)
    y_test = sc.transform(y_test)

    # Model Training and Evaluation
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest Regressor": RandomForestRegressor(n_estimators=200, max_depth=5, random_state=0),
        "Decision Tree Regressor": DecisionTreeRegressor(random_state=0)
    }

    for name, model in models.items():
        model.fit(x_train, y_train.ravel())
        y_pred = sc.inverse_transform(model.predict(x_test).reshape(-1, 1))
        st.write(f"Model: {name}")
        st.write("Train Score:", model.score(x_train, y_train) * 100)
        st.write("Test Score:", model.score(x_test, y_test) * 100)
        
        st.write(f"Hasil Prediksi untuk Model {name}")
        st.write("Berikut adalah visualisasi hasil prediksi vs actual.")
        fig, ax = plt.subplots(figsize=(16, 8))
        sns.distplot(sc.inverse_transform(y_test), hist=False, label='Actual', ax=ax)
        sns.distplot(y_pred, hist=False, label='Predicted', ax=ax)
        plt.legend()
        st.pyplot(fig)
        
        # Penjelasan Linear Regression dan hasil grafik
        if name == "Linear Regression":
            st.subheader('Hasil Prediksi Model Linear Regression')
            st.text("Linear Regression adalah metode statistik yang digunakan untuk memodelkan hubungan antara satu atau lebih variabel independen (misalnya suhu rata-rata, curah hujan, kelembapan) dengan variabel dependen (yaitu produksi padi). Tujuan dari model ini adalah untuk memprediksi nilai produksi padi berdasarkan variabel-variabel tersebut.")
            st.text("Grafik ini menunjukkan hasil prediksi model Linear Regression terhadap nilai aktual produksi padi. Grafik densitas ini membandingkan distribusi nilai aktual (dalam warna biru) dengan distribusi nilai prediksi (dalam warna oranye).")
            st.text("Sumbu horizontal (x) menunjukkan nilai produksi padi, sementara sumbu vertikal (y) menunjukkan densitas atau seberapa sering nilai tersebut muncul dalam data.")
            st.text("Jika garis oranye (prediksi) dekat dengan garis biru (aktual), ini menunjukkan bahwa model Linear Regression cukup akurat dalam memprediksi produksi padi.")
            st.text("Grafik ini membantu kita memahami sejauh mana nilai prediksi mendekati nilai aktual, yang penting untuk mengevaluasi kinerja model Linear Regression.")
            st.text("Dengan menggunakan model Linear Regression, kita dapat memprediksi produksi padi di masa depan berdasarkan variabel-variabel iklim dan pertanian. Ini sangat berguna untuk perencanaan pertanian dan pengambilan keputusan strategis.")
            st.text("Model ini membantu kita mengantisipasi perubahan produksi padi berdasarkan perubahan lingkungan, yang bisa sangat bermanfaat dalam menghadapi variabilitas iklim.")
        
        if name == "Random Forest Regressor":
            # Visualisasi Hasil Prediksi Model Random Forest Regressor
            st.subheader('Hasil Prediksi Model Random Forest Regressor')
            st.text("Random Forest Regressor adalah metode ensemble yang menggunakan beberapa pohon keputusan untuk meningkatkan akurasi prediksi. Model ini bekerja dengan menggabungkan hasil dari banyak pohon keputusan untuk memberikan prediksi yang lebih baik dan lebih akurat.")
            st.text("Grafik ini menunjukkan hasil prediksi model Random Forest Regressor terhadap nilai aktual produksi padi. Grafik densitas ini membandingkan distribusi nilai aktual (dalam warna biru) dengan distribusi nilai prediksi (dalam warna oranye).")
            st.text("Sumbu horizontal (x) menunjukkan nilai produksi padi, sementara sumbu vertikal (y) menunjukkan densitas atau seberapa sering nilai tersebut muncul dalam data.")
            st.text("Jika garis oranye (prediksi) dekat dengan garis biru (aktual), ini menunjukkan bahwa model Random Forest Regressor cukup akurat dalam memprediksi produksi padi.")
            st.text("Grafik ini membantu kita memahami sejauh mana nilai prediksi mendekati nilai aktual, yang penting untuk mengevaluasi kinerja model Random Forest Regressor.")
            st.text("Dengan menggunakan model Random Forest Regressor, kita dapat memprediksi produksi padi di masa depan berdasarkan variabel-variabel iklim dan pertanian. Ini sangat berguna untuk perencanaan pertanian dan pengambilan keputusan strategis.")
            st.text("Model ini membantu kita mengantisipasi perubahan produksi padi berdasarkan perubahan lingkungan, yang bisa sangat bermanfaat dalam menghadapi variabilitas iklim.")

        if name ==  "Decision Tree Regressor":
            # Visualisasi Hasil Prediksi Model Decision Tree Regressor
            st.subheader('Hasil Prediksi Model Decision Tree Regressor')
            st.text("Decision Tree Regressor adalah model prediktif yang menggunakan pohon keputusan untuk memprediksi nilai output berdasarkan aturan if-then dari fitur input. Model ini membagi data ke dalam beberapa bagian untuk menghasilkan prediksi yang lebih tepat.")
            st.text("Grafik ini menunjukkan hasil prediksi model Decision Tree Regressor terhadap nilai aktual produksi padi. Grafik densitas ini membandingkan distribusi nilai aktual (dalam warna biru) dengan distribusi nilai prediksi (dalam warna oranye).")
            st.text("Sumbu horizontal (x) menunjukkan nilai produksi padi, sementara sumbu vertikal (y) menunjukkan densitas atau seberapa sering nilai tersebut muncul dalam data.")
            st.text("Jika garis oranye (prediksi) dekat dengan garis biru (aktual), ini menunjukkan bahwa model Decision Tree Regressor cukup akurat dalam memprediksi produksi padi.")
            st.text("Grafik ini membantu kita memahami sejauh mana nilai prediksi mendekati nilai aktual, yang penting untuk mengevaluasi kinerja model Decision Tree Regressor.")
            st.text("Dengan menggunakan model Decision Tree Regressor, kita dapat memprediksi produksi padi di masa depan berdasarkan variabel-variabel iklim dan pertanian. Ini sangat berguna untuk perencanaan pertanian dan pengambilan keputusan strategis.")
            st.text("Model ini membantu kita mengantisipasi perubahan produksi padi berdasarkan perubahan lingkungan, yang bisa sangat bermanfaat dalam menghadapi variabilitas iklim.")

    # Decision Tree Regressor dengan parameter yang disesuaikan
    DTreeReg_model = DecisionTreeRegressor(splitter='best', min_samples_split=8, min_samples_leaf=5, max_features=None, max_depth=2, random_state=0)
    DTreeReg_model.fit(x_train, y_train)

    # Prediksi dan Visualisasi
    ypred_DTreeReg_model = sc.inverse_transform(DTreeReg_model.predict(x_test).reshape(-1, 1))
    ypred_DTreeReg_model = pd.DataFrame(ypred_DTreeReg_model)

    st.write("Model: Decision Tree Regressor dengan Parameter Khusus")
    st.write("Train Score:", DTreeReg_model.score(x_train, y_train) * 100)
    st.write("Test Score:", DTreeReg_model.score(x_test, y_test) * 100)

    st.write("Berikut adalah visualisasi hasil prediksi vs actual untuk Model Decision Tree Regressor.")
    fig, ax = plt.subplots(figsize=(16, 8))
    sns.distplot(sc.inverse_transform(y_test), hist=False, label='Actual', ax=ax)
    sns.distplot(ypred_DTreeReg_model, hist=False, label='Predicted', ax=ax)
    plt.legend()
    st.pyplot(fig)

    # Penjelasan Decision Tree Regressor dengan parameter khusus dan hasil grafik
    st.subheader('Hasil Prediksi Model Decision Tree Regressor dengan Parameter Khusus')
    st.text("Decision Tree Regressor adalah model prediktif yang menggunakan pohon keputusan untuk memprediksi nilai output berdasarkan aturan if-then dari fitur input. Model ini membagi data ke dalam beberapa bagian untuk menghasilkan prediksi yang lebih tepat.")
    st.text("Grafik ini menunjukkan hasil prediksi model Decision Tree Regressor dengan parameter khusus terhadap nilai aktual produksi padi. Grafik densitas ini membandingkan distribusi nilai aktual (dalam warna biru) dengan distribusi nilai prediksi (dalam warna oranye).")
    st.text("Sumbu horizontal (x) menunjukkan nilai produksi padi, sementara sumbu vertikal (y) menunjukkan densitas atau seberapa sering nilai tersebut muncul dalam data.")
    st.text("Jika garis oranye (prediksi) dekat dengan garis biru (aktual), ini menunjukkan bahwa model Decision Tree Regressor dengan parameter khusus cukup akurat dalam memprediksi produksi padi.")
    st.text("Grafik ini membantu kita memahami sejauh mana nilai prediksi mendekati nilai aktual, yang penting untuk mengevaluasi kinerja model Decision Tree Regressor.")
    st.text("Dengan menggunakan model Decision Tree Regressor dengan parameter khusus, kita dapat memprediksi produksi padi di masa depan berdasarkan variabel-variabel iklim dan pertanian. Ini sangat berguna untuk perencanaan pertanian dan pengambilan keputusan strategis.")
    st.text("Model ini membantu kita mengantisipasi perubahan produksi padi berdasarkan perubahan lingkungan, yang bisa sangat bermanfaat dalam menghadapi variabilitas iklim.")

if __name__ == "__main__":
    main()
