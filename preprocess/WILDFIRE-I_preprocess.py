import os
import os.path as osp
from natsort import natsorted
import csv

img_suffix = 'WILDFIRE-I/Images'
label_suffix = 'WILDFIRE-I/Labels'

label_li = os.listdir(label_suffix)
label_li = natsorted(label_li)

for label in label_li:
    f = open(osp.join(label_suffix, label), 'r')
    rdr = csv.reader(f)
    info = f.readline()[:-1].split(' ')
    cls, x, y, w, h = [float(i) for i in info]
    f.close()
    
    if cls == 1:
        os.remove(osp.join(label_suffix, label))
        os.remove(osp.join(img_suffix, label.split('.')[0]+'.jpg'))