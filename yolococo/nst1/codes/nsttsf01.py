import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import cv2
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
models = ["andy.jpg", "candy.jpg", "composition.jpg", "la_muse.jpg", "mosaic.jpg"
          , "starry_night.jpg", "the_wave.jpg", "ss.jpg", "ss2.jpg", "ss3.jpg"]
outs=[]
content_image=cv2.imread('../../data/IMG_2997.png')
# 將影像縮成 1/4
content_image = cv2.resize(content_image, (0, 0), None, 0.5, 0.5)
cv2.imshow("original", content_image)
h,w,c = content_image.shape
# 使用numpy來轉成float32 numpy array，加上批次維度，並正規化到[0,1]的區間大小
content_image = content_image.astype(np.float32)[np.newaxis, ...] / 255.
for i in range(0,len(models)):
    style_image=cv2.imread('../models/'+ models[i])
    style_image = style_image.astype(np.float32)[np.newaxis, ...] / 255.
    # 將style image 轉成256 pixels (模式訓練時用的大小), content image 可以任意大小
    style_image = tf.image.resize(style_image, (256, 256))
    # 載入stylization模式
    model = hub.load('../')
    # 得到結果並show出來
    out_image = model(tf.constant(content_image), tf.constant(style_image))
    outs.append(np.squeeze(out_image))
imgStack = cv2.hconcat(outs[0:5])
imgStack2 = cv2.hconcat(outs[5:10])
imgStack3 = cv2.vconcat([imgStack, imgStack2])
# for i in range(0,len(models)//2):
#     cv2.putText(imgStack3, models[i], ((10 + w * i), 20), 4, 0.6, (0, 255, 255), 1)
#     cv2.putText(imgStack3, models[i+5], ((10 + w * i), 20+h), 4, 0.6, (0, 0, 255), 1)
cv2.imshow("Output", np.squeeze(imgStack3))
cv2.waitKey(0)
