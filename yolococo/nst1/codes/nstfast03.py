import cv2
import time
models = ["la_muse.t7","the_scream.t7","composition_vii.t7","starry_night.t7","la_muse_eccv16.t7"
          ,"udnie.t7","mosaic.t7","candy.t7","feathers.t7","the_wave.t7"]
outs=[]
nets = []
# 讀取webcam
cap = cv2.VideoCapture(0)
while True:
    prev_time = time.time()
    success, image = cap.read()
    image = cv2.resize(image,(0, 0), None, 0.2, 0.2)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1.0, (w, h), (103.939, 116.779, 123.680), swapRB=True, crop=False)
    for i in range(0,len(models)):
        net = cv2.dnn.readNetFromTorch('../models/'+models[i])
        net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
        # 進行計算
        net.setInput(blob)
        out = net.forward()
        out = out.reshape(3, out.shape[2], out.shape[3])
        out[0] += 103.939
        out[1] += 116.779
        out[2] += 123.68
        out /= 255
        out = out.transpose(1, 2, 0)
        outs.append(out)
    imgStack = cv2.hconcat(outs[0:5])
    imgStack2 = cv2.hconcat(outs[5:10])
    imgStack3 = cv2.vconcat([imgStack, imgStack2])
    print(1 / (time.time() - prev_time))
    cv2.imshow("output", imgStack3)
    cv2.imshow("original", image)
    outs =[]
    if cv2.waitKey(1) & 0xFF == 27:
        cap.release()
