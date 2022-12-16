import cv2
import streamlit as st

cap = cv2.VideoCapture(0)

st.title('Streamlit + CV2')
run = st.checkbox('請打勾來執行')
FRAME_WINDOW = st.image([])

while run:
    success, frame = cap.read()
    FRAME_WINDOW.image(frame, channels= 'BGR')

cap.release()
