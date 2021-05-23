import cv2
import pytesseract
import streamlit as st
from PIL import Image
st.image('cover.png')
st.title('OCR APP')
st.subheader('Developed by Adil')
st.write('This app is under Development')
file=st.file_uploader('Upload a File',type=['png','jpeg'])


if file is None:
	st.write('No file uploaded')
else:
	convert_img=Image.open(file).convert('RGB')
	st.header('Uploaded Image')
	st.image(convert_img,width=400)
	custom_config = r'--oem 3 --psm 6'
	if st.button('Perform OCR'):
		res=pytesseract.image_to_string(convert_img, config=custom_config)
		st.header('Output')
		st.write(res)
