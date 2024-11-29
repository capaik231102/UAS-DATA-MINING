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

# Fungsi evaluasi model
def evaluate_models(models, x_train, x_test, y_train, y_test, sc):
    results = {}
    for name, model in models.items():
        model.fit(x_train, y_train.ravel())
        y_pred = sc.inverse_transform(model.predict(x_test).reshape(-1, 1))
        train_score = model.score(x_train, y_train) * 100
        test_score = model.score(x_test, y_test) * 100
        mse = mean_squared_error(sc.inverse_transform(y_test), y_pred)
        r2 = r2_score(sc.inverse_transform(y_test), y_pred)

        results[name] = {
            "Train Score": train_score,
            "Test Score": test_score,
            "MSE": mse,
            "R2": r2,
            "y_pred": y_pred
        }
    return results

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

    # Model Training
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest Regressor": RandomForestRegressor(n_estimators=200, max_depth=5, random_state=0),
        "Decision Tree Regressor": DecisionTreeRegressor(random_state=0),
        "Decision Tree Regressor with Special Parameters": DecisionTreeRegressor(splitter='best', min_samples_split=8, min_samples_leaf=5, max_features=None, max_depth=2, random_state=0)
    }

    # Evaluate Models
    results = evaluate_models(models, x_train, x_test, y_train, y_test, sc)

    # Page for Model Evaluation
    st.title("Evaluasi Model")
    st.write("Halaman ini membandingkan kinerja keempat model yang telah dibuat.")

    eval_data = {
        "Model": [],
        "Train Score (%)": [],
        "Test Score (%)": [],
        "MSE": [],
        "R2": []
    }

    for name, result in results.items():
        eval_data["Model"].append(name)
        eval_data["Train Score (%)"].append(result["Train Score"])
        eval_data["Test Score (%)"].append(result["Test Score"])
        eval_data["MSE"].append(result["MSE"])
        eval_data["R2"].append(result["R2"])

    eval_df = pd.DataFrame(eval_data)
    st.dataframe(eval_df)

    st.write("### Grafik Perbandingan Prediksi vs Nilai Aktual")

    fig, ax = plt.subplots(figsize=(16, 8))
    sns.distplot(sc.inverse_transform(y_test), hist=False, label='Actual', ax=ax)

    for name, result in results.items():
        sns.distplot(result["y_pred"], hist=False, label=name, ax=ax)

    plt.legend()
    st.pyplot(fig)

    st.title("Kesimpulan dan Rekomendasi Pengambilan Keputusan")

    st.header("Kesimpulan Analisis Produksi Padi")

    st.subheader("Model Terbaik")
    st.write("""
    Berdasarkan hasil evaluasi model, **Linear Regression** adalah model terbaik untuk memprediksi produksi padi. Model ini memiliki keseimbangan terbaik antara Train Score (85.86%), Test Score (88.54%), dan nilai Mean Squared Error (MSE) terendah (143,534,153,105.49). Ini menunjukkan bahwa Linear Regression mampu memberikan prediksi yang paling akurat dan stabil dibandingkan model lainnya.
    """)

    st.subheader("Overfitting pada Model")
    st.write("""
    Model **Decision Tree Regressor** menunjukkan tanda-tanda overfitting dengan Train Score yang sangat tinggi (99.95%) tetapi Test Score yang lebih rendah (82.49%). Ini menunjukkan bahwa model ini terlalu menyesuaikan dengan data pelatihan dan tidak generalisasi dengan baik pada data baru.
    Model **Random Forest Regressor** juga menunjukkan sedikit overfitting dengan Train Score yang sangat tinggi (95.81%) dan Test Score yang lebih rendah (85.55%).
    """)

    st.subheader("Keandalan Model")
    st.write("""
    Model **Decision Tree Regressor dengan Parameter Khusus** memiliki performa yang lebih seimbang dibandingkan dengan Decision Tree Regressor biasa, tetapi masih tidak sebaik Linear Regression dalam hal akurasi prediksi pada data pengujian.
    """)

    st.header("Rekomendasi Pengambilan Keputusan")

    st.subheader("Menggunakan Model Linear Regression")
    st.write("""
    Disarankan untuk menggunakan model Linear Regression untuk prediksi produksi padi di masa mendatang karena model ini memberikan hasil prediksi yang paling akurat dan dapat diandalkan.
    """)

    st.subheader("Peningkatan Data dan Model")
    st.write("""
    Teruslah memperbarui dan memperkaya data yang digunakan dalam model untuk meningkatkan akurasi dan relevansi prediksi.
    Pertimbangkan untuk menggabungkan lebih banyak faktor atau variabel yang mungkin mempengaruhi produksi padi untuk memperbaiki model lebih lanjut.
    """)

    st.subheader("Penggunaan Model untuk Pengambilan Keputusan")
    st.write("""
    Gunakan prediksi dari model ini untuk membantu dalam perencanaan strategis, alokasi sumber daya, dan pengambilan keputusan terkait produksi padi. Prediksi yang akurat akan membantu mengantisipasi kebutuhan dan merencanakan produksi secara lebih efisien.
    """)

    st.subheader("Monitoring dan Evaluasi")
    st.write("""
    Lakukan monitoring dan evaluasi berkala terhadap performa model untuk memastikan model tetap akurat dan relevan dengan kondisi terbaru. Sesuaikan model jika diperlukan berdasarkan hasil evaluasi tersebut.
    """)

if __name__ == "__main__":
    main()
