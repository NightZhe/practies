import cv2
models = ["la_muse.t7","the_scream.t7","composition_vii.t7","starry_night.t7","la_muse_eccv16.t7"
          ,"udnie.t7","mosaic.t7","candy.t7","feathers.t7","the_wave.t7"]
outs=[]
# 讀取圖片
image = cv2.imread('../../data/IMG_2997.png')
image = cv2.resize(image,(0, 0), None, 0.4,0.4)
h,w,c = image.shape
print(image.shape)
blob = cv2.dnn.blobFromImage(image, 1.0, (w, h), (103.939, 116.779, 123.680), swapRB=False, crop=False)

for i in range(0,len(models)):
    # 加載模型
    net = cv2.dnn.readNetFromTorch('../models/'+ models[i])
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
# 輸出圖片
imgStack = cv2.hconcat(outs[0:5])
imgStack2 = cv2.hconcat(outs[5:10])
imgStack3 = cv2.vconcat([imgStack, imgStack2])
# for i in range(0,len(models)//2):
    # cv2.putText(imgStack3, models[i], ((10 + w * i), 20), 4, 0.6, (100, 10, 255), 1)
    # cv2.putText(imgStack3, models[i+5], ((10 + w * i), 20+h), 4, 0.6, (0, 0, 255), 1)
cv2.imshow("Styled images", imgStack3)
cv2.waitKey(0)
