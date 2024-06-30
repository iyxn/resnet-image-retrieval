from PIL import Image
from utils.feature_extractor import FeatureExtractor
import glob
import numpy as np
import streamlit as st

st.title("Ekstraksi Fitur")

fe = FeatureExtractor()
img_paths = glob.glob("data/*")

def extract_features():
    features = []
    img_paths = glob.glob("data/*")
    progress_bar = st.progress(0)
    total_images = len(img_paths)
    percentage_text = st.empty()
    
    for i, img_path in enumerate(img_paths):
        progress = (i + 1) / total_images
        progress_bar.progress(progress)
        percentage_text.write(f"Progress: {int(progress * 100)}%")
        img = Image.open(img_path)
        feature = fe.extract(img)
        features.append(feature)

    np.save("features/features_resnet50.npy", features)

st.write("Untuk menyesuaikan dengan data yang anda akan gunakan, proses ekstraksi fitur harus dilakukan.")
st.write("Pastikan mengikuti langkah-langkah dibawah ini:")
st.write("  1. Hapus semua data yang ada di dalam folder data.")
st.write("  2. Masukan data gambar yang ingin anda ekstrak fiturnya ke dalam folder data.")
st.write("  3. Klik Mulai dan saat selesai akan terdapat file features_resnet50.npy di dalam folder features.")
st.write("  4. Image retrieval dengan data yang sudah di sesuaikan sudah siap.")

st.write("Klik Mulai jika sudah mengikuti step diatas.")
button = st.button(label="Mulai")

if button:
    extract_features()
    st.success("Proses ekstrak fitur selesai")