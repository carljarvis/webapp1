import streamlit as st
from PIL import Image

camera_image = st.camera_input('camera')
print(camera_image)

img =  Image.open(camera_image)
gray_img = img.convert('L')
st.image(gray_img)
