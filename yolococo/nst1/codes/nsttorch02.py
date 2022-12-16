import re
import cv2
import time
import torch
from torchvision import transforms
from trans_net import TransformerNet
models = ["candy.pth", "mosaic.pth", "rain_princess.pth", "udnie.pth"]
outs=[]
content_transform = transforms.Compose([transforms.ToTensor(),transforms.Lambda(lambda x: x.mul(255))])
# 讀取圖片與模型
cap = cv2.VideoCapture(0)
while True:
    prev_time = time.time()
    success, image = cap.read()
    image = cv2.resize(image, (500, 280))
    (h, w) = image.shape[:2]
    style_model = TransformerNet()
    state_dict = torch.load('../models/'+models[2])
    for k in list(state_dict.keys()):
        if re.search(r'in\d+\.running_(mean|var)$', k):
            del state_dict[k]
    style_model.load_state_dict(state_dict)
    style_model.to('cpu')
    style_model.eval()
    # 進行計算
    content_image = content_transform(image)
    content_image = content_image.unsqueeze(0).to('cpu')
    with torch.no_grad():
        output = style_model(content_image).cpu()
    # 輸出圖片
    img = output[0].clamp(0, 255).numpy().transpose(1, 2, 0).astype("uint8")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    print(1 / (time.time() - prev_time))
    cv2.imshow("output", img)
    cv2.imshow("original", image)
    if cv2.waitKey(1) & 0xFF == 27:
        cap.release()