# BERTopic - Surat Al Baqarah

## 📌 Deskripsi
Project ini menggunakan **BERTopic** untuk melakukan *topic modeling* pada dataset **Surat Al-Baqarah** (286 ayat).  
Tujuan utama adalah membandingkan hasil topik dari pendekatan modern (BERTopic) dengan pendekatan klasik (LDA), serta menampilkan hasil melalui web interface berbasis Flask.

---

## 📂 Struktur Folder
bertopic_project/
│
├── app.py                  # Flask web interface
├── train_bertopic.py       # Script untuk melatih model BERTopic
├── requirements.txt        # Daftar library
├── bertopic_model/         # Model hasil training
├── data/
│   └── al_baqarah.json     # Dataset (286 ayat)
├── templates/
│   ├── index.html          # Input jumlah topik
│   └── result.html         # Hasil topik
├── static/
│   └── style.css           # (opsional) styling web
└── screenshots/            # (opsional) dokumentasi hasil

---

## ⚙️ Instalasi
1. Clone repo ini atau download folder project.
2. Buat virtual environment (Python 3.11.9 disarankan).
3. Install library:
   ```bash
   pip install -r requirements.txt

🚀 Cara Menjalankan
1. Training model BERTopic  
Jalankan script:
python train_bertopic.py
Model akan tersimpan di folder bertopic_model/.

2. Menjalankan web interface  
Jalankan:
python app.py
Buka browser di http://127.0.0.1:5000/.

3. Input jumlah topik  
Masukkan jumlah topik yang ingin ditampilkan.
Catatan: BERTopic menghasilkan jumlah topik otomatis sesuai data. Jika ingin memaksa jumlah tertentu, gunakan:
topic_model.reduce_topics(docs, nr_topics=10)

📸 Screenshots (opsional)
- Tampilan halaman input (index.html)
- Tampilan hasil topik (result.html)

📚 Library Utama
- Flask
- BERTopic
- UMAP-learn
- HDBSCAN
- Transformers
- scikit-learn
- numpy, pandas
