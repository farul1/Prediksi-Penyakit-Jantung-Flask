import os
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, render_template

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# --- Muat Model dan Kolom ---
# Muat model yang sudah dilatih
model_path = os.path.join('save_model', 'heart_disease_model.pkl')
model = pickle.load(open(model_path, 'rb'))

# Muat daftar kolom yang digunakan saat training
columns_path = os.path.join('save_model', 'model_columns.pkl')
model_columns = pickle.load(open(columns_path, 'rb'))


# --- Route untuk Halaman Utama ---
@app.route('/')
def home():
    # Tampilkan halaman utama dengan form input
    return render_template('index.html')


# --- Route untuk Prediksi ---
@app.route('/predict', methods=['POST'])
def predict():
    # Buat DataFrame kosong dengan kolom yang sama persis seperti saat training
    input_df = pd.DataFrame(columns=model_columns)
    # Isi semua kolom dengan nilai 0 untuk baris pertama
    input_df.loc[0] = 0

    # --- Ambil dan Proses Input dari Form ---
    # Ambil nilai numerik langsung
    input_df.at[0, 'age'] = int(request.form['age'])
    input_df.at[0, 'sex'] = int(request.form['sex'])
    input_df.at[0, 'trestbps'] = int(request.form['trestbps'])
    input_df.at[0, 'chol'] = int(request.form['chol'])
    input_df.at[0, 'fbs'] = int(request.form['fbs'])
    input_df.at[0, 'restecg'] = int(request.form['restecg'])
    input_df.at[0, 'thalch'] = int(request.form['thalch'])
    input_df.at[0, 'exang'] = int(request.form['exang'])
    input_df.at[0, 'oldpeak'] = float(request.form['oldpeak'])
    input_df.at[0, 'ca'] = int(request.form['ca'])

    # Proses input yang di-one-hot-encode
    # Gabungkan nama kolom dengan nilai dari form, lalu set nilainya menjadi 1
    # Contoh: jika cp = 'typical angina', maka kolom 'cp_typical angina' akan menjadi 1
    
    # Untuk 'cp' (Chest Pain)
    cp_value = 'cp_' + request.form['cp']
    if cp_value in model_columns:
        input_df.at[0, cp_value] = 1

    # Untuk 'slope'
    slope_value = 'slope_' + request.form['slope']
    if slope_value in model_columns:
        input_df.at[0, slope_value] = 1

    # Untuk 'thal'
    thal_value = 'thal_' + request.form['thal']
    if thal_value in model_columns:
        input_df.at[0, thal_value] = 1
    
    # Lakukan prediksi menggunakan model
    prediction = model.predict(input_df)
    prediction_proba = model.predict_proba(input_df)

    # Ambil hasil prediksi (0 atau 1)
    hasil_prediksi = prediction[0]
    
    # Ambil probabilitas untuk kelas 1 (risiko tinggi)
    probabilitas = prediction_proba[0][1]

    # Tentukan pesan hasil
    if hasil_prediksi == 1:
        result = f"Pasien ini berisiko tinggi memiliki penyakit jantung (Probabilitas: {probabilitas*100:.2f}%)"
    else:
        result = f"Pasien ini berisiko rendah memiliki penyakit jantung (Probabilitas Risiko Tinggi: {probabilitas*100:.2f}%)"

    # Kirim hasil ke halaman result.html
    return render_template('result.html', prediction_text=result)


# Jalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)