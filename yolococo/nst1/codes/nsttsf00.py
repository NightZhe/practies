import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import cv2
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
# 將content_image轉成style_image的樣式，先用CV2載入兩個圖樣
content_image = cv2.imread('../../data1/IMG_2997.png')
cv2.imshow("original", content_image)
content_image = cv2.cvtColor(content_image, cv2.COLOR_BGR2RGB)
style_image = cv2.imread('../models/ss.jpg')
cv2.imshow("style", style_image)
# 使用numpy來轉成float32 numpy array，加上批次維度，並正規化到[0,1]的區間大小
content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.
style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.
# 將style image 轉成256 pixels (模式訓練時用的大小), content image 可以任意大小
style_image = tf.image.resize(style_image, (256, 256))
# 載入stylization模式
# model = hub.load('https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2')
model = hub.load('../')
# 得到結果並show出來
out_image = model(tf.constant(content_image), tf.constant(style_image))
img = cv2.cvtColor(np.squeeze(out_image), cv2.COLOR_RGB2BGR)
cv2.imshow("Output", img)
cv2.waitKey(0)
