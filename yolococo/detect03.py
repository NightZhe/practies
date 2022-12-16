# detect03.py
import torch
import numpy as np
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom',
                       path='yolov5/runs/train/exp2/weights/best.pt', force_reload=True)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue
    frame = cv2.resize(frame, (800, 480))
    results = model(frame)
    # print(np.array(results.render()).shape)
    cv2.imshow('YOLO COCO 03 mask detection', np.squeeze(results.render()))
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()
