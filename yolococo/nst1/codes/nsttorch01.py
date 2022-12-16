import re
import cv2
import torch
from torchvision import transforms
from trans_net import TransformerNet
models = ["candy.pth", "mosaic.pth", "rain_princess.pth", "udnie.pth"]
outs=[]
# 讀取圖片與模型
content_image = cv2.imread('../../data/IMG_2997.png')
content_image = cv2.cvtColor(content_image, cv2.COLOR_BGR2RGB)
content_image = cv2.resize(content_image, (0, 0), None, 0.5, 0.5)
content_transform = transforms.Compose([transforms.ToTensor(),transforms.Lambda(lambda x: x.mul(255))])
content_image2 = content_transform(content_image)
content_image2 = content_image2.unsqueeze(0).to('cpu')
style_model = TransformerNet()

for i in range(0,len(models)):
    state_dict = torch.load('../models/'+models[i])
    for k in list(state_dict.keys()):
        if re.search(r'in\d+\.running_(mean|var)$', k):
            del state_dict[k]
    style_model.load_state_dict(state_dict)
    style_model.to('cpu')
    style_model.eval()
    # 進行計算
    with torch.no_grad():
        output = style_model(content_image2).cpu()
    # 輸出圖片
    img = output[0].clamp(0, 255).numpy().transpose(1, 2, 0).astype("uint8")
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    outs.append(img)
imgStack = cv2.hconcat(outs[0:4])
cv2.imshow("Styled images", imgStack)
cv2.waitKey(0)