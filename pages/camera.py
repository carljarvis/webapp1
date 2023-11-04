import streamlit as st
from PIL import Image

st.subheader('Color to greyscale converter')

uploaded_image = st.file_uploader('Upload Image')




with st.expander('Start Camera'):
    camera_image = st.camera_input('camera')
    print(camera_image)

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_uploaded_img = img.convert('L')
    st.image(gray_uploaded_img)

if camera_image:# != None:

    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)


