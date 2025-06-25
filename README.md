# 🫀 Aplikasi Web Prediksi Penyakit Jantung dengan Flask

Aplikasi web sederhana yang dibangun menggunakan **Python** dan **Flask** untuk memprediksi risiko penyakit jantung berdasarkan data medis. Model yang digunakan adalah **Random Forest Classifier** yang telah dilatih menggunakan dataset **Heart Disease UCI**.

---

## 📸 Tampilan Aplikasi

| Halaman Input | Halaman Hasil |
|---------------|---------------|
| *(Screenshot `index.html` di sini)* | *(Screenshot `result.html` di sini)* |

---

## ✨ Fitur Utama

- 🧾 **Form Input Interaktif** — Pengguna dapat memasukkan 13 parameter medis untuk mendapatkan hasil prediksi.
- ⚡ **Prediksi Real-time** — Hasil prediksi ditampilkan langsung menggunakan model machine learning.
- 📊 **Visualisasi Performa** — Menampilkan confusion matrix untuk evaluasi model secara visual.
- 💻 **Antarmuka Sederhana** — Dibuat menggunakan HTML dan CSS agar mudah digunakan dan ringan diakses.

---

## ⚙️ Teknologi yang Digunakan

- **Backend**: Flask (Python)
- **Machine Learning**: Scikit-learn
- **Manipulasi Data**: Pandas, NumPy
- **Visualisasi**: Matplotlib, Seaborn
- **Frontend**: HTML, CSS

---

## 🚀 Cara Menjalankan Proyek Ini

### 1. Persiapan Awal

- Pastikan sudah terinstal Python versi 3.8 ke atas.
- Clone repositori ini atau unduh sebagai ZIP.
- Letakkan file `heart.csv` di folder utama proyek.

### 2. Setup Lingkungan Virtual

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan environment
# Windows
venv\Scripts\activate.bat
# macOS / Linux
source venv/bin/activate

# Install dependensi
pip install -r requirements.txt
