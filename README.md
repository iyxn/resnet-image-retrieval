
# RESNET IMAGE RETRIEVAL

Implementasi Image Retrieval dengan feature extractor ResNet50.

# Fitur
## Halaman Pencarian
![App Screenshot](https://raw.githubusercontent.com/iyxn/resnet-image-retrieval/development/screenshoot/Home.png)
![App Screenshot](https://raw.githubusercontent.com/iyxn/resnet-image-retrieval/development/screenshoot/retrieved.png)

## Ekstraksi Fitur
Digunakan untuk menyesuaikan dengan data anda dikarenakan data default yang digunakan adalah dataset pakaian.
![App Screenshot](https://raw.githubusercontent.com/iyxn/resnet-image-retrieval/development/screenshoot/feature_extraction.png)


# Instalasi

Clone repository ini

```bash
  git clone https://github.com/iyxn/resnet-image-retrieval.git
  cd resnet-image-retrieval
```
Install library yang diperlukan
```bash
  pip install -r requirements.txt
```
Jalankan
```bash
  streamlit run "Home.py"
```
# Catatan Penting

Untuk menyesuaikan dengan data yang anda akan gunakan, proses ekstraksi fitur harus dilakukan.

Pastikan mengikuti langkah-langkah dibawah ini:

- Hapus semua data yang ada di dalam folder data.
- Masukan data gambar yang ingin anda ekstrak fiturnya ke dalam folder data.
- Klik Mulai dan saat selesai akan terdapat file features_resnet50.npy di dalam folder features.
Image retrieval dengan data yang sudah di sesuaikan sudah siap.

# Dataset default
https://www.kaggle.com/datasets/vikashrajluhaniwal/fashion-images