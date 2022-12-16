import cv2
import streamlit as st
models = ["la_muse.t7","the_scream.t7","composition_vii.t7","starry_night.t7","la_muse_eccv16.t7"
          ,"udnie.t7","mosaic.t7","candy.t7","feathers.t7","the_wave.t7"]
outs=[]
nets = []
cap = cv2.VideoCapture(0)
st.title('Streamlit + CV2 + Style Transfer')
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
STYLE_WINDOW = st.image([])
net = cv2.dnn.readNetFromTorch('../models/'+models[3])
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
while run:
    success, frame = cap.read()
    image = cv2.resize(frame, (500, 280))
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1.0, (w, h), (103.939, 116.779, 123.680), swapRB=False, crop=False)
    # 進行計算
    net.setInput(blob)
    out = net.forward()
    out = out.reshape(3, out.shape[2], out.shape[3])
    out[0] += 103.939
    out[1] += 116.779
    out[2] += 123.68
    out /= 255
    out = out.transpose(1, 2, 0)
    FRAME_WINDOW.image(image, channels='BGR')
    STYLE_WINDOW.image(out, clamp=True, channels='BGR')

cap.release()
