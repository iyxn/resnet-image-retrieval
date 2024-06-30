import streamlit as st
from itertools import cycle
from utils.calculate_similarity import upload_images

st.set_page_config(
    page_title = "Image Retrieval", layout = "wide")
st.title('Image Retrieval System')

def show_retrieved(img):
    extract_feature =  upload_images(img)
    filteredImages = [item[1] for item in extract_feature]
    print(filteredImages)
    cols = cycle(st.columns(4))
    for idx, filteredImage in enumerate(filteredImages):
        next(cols).image(filteredImage, width=150)


image_upload = st.file_uploader("Pilih Gambar...", type=["jpg", "jpeg"])

if image_upload:
    st.subheader("Gambar yang dicari:")
    st.image(image_upload, width=150)
    st.subheader("Hasil Pencarian:")
    st.success("Pencarian gambar selesai")
    show_retrieved(image_upload)
    