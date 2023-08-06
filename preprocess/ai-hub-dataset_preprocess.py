import os
import os.path as osp
from natsort import natsorted

img_suffix = 'custom_dataset/images'
label_suffix = 'custom_dataset/labels'

img_li = os.listdir(img_suffix)
img_li = natsorted(img_li)

tmp = "-1"

for img in img_li:
    cur = img.split('_')[0]
    
    if cur != tmp:
        tmp = cur
        continue
    else:
        img_path = osp.join(img_suffix, img)
        label_path = osp.join(label_suffix, img.split('.')[0]+'.txt')
        os.remove(img_path)
        os.remove(label_path)