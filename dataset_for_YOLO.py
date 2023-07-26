import os
from natsort import natsorted
import csv
from tqdm import tqdm
from sklearn.model_selection import train_test_split
import shutil

def get_XY(img_path, label_path):
    
    img_li = os.listdir(img_path)
    img_li = natsorted(img_li)
    label_li = os.listdir(label_path)
    label_li = natsorted(label_li)
    
    img_path_li = []
    label_path_li = []
    
    for cur in img_li:
        cur_img = os.path.join(img_path, cur)
        img_path_li.append(cur_img)
        
    for cur in label_li:
        cur_label = os.path.join(label_path, cur)
        label_path_li.append(cur_label)
        
    return img_path_li, label_path_li
    

if __name__ == '__main__':
    
    data_root = 'dataset'
    image_path = os.path.join(data_root, "images")
    label_path = os.path.join(data_root, "labels")
    classes = os.listdir(image_path)
        
    flame_img_path = os.path.join(image_path, "flame")
    flame_label_path = os.path.join(label_path, "flame")
    
    smoke_img_path = os.path.join(image_path, "smoke")
    smoke_label_path = os.path.join(label_path, "smoke")
    
    flame_X, flame_y = get_XY(flame_img_path, flame_label_path)
    smoke_X, smoke_y = get_XY(smoke_img_path, smoke_label_path)
    
    flame_X_train, flame_X_val, flame_y_train, flame_y_val = \
        train_test_split(flame_X, flame_y, test_size=0.2, shuffle=True, random_state=42)
    smoke_X_train, smoke_X_val, smoke_y_train, smoke_y_val = \
        train_test_split(smoke_X, smoke_y, test_size=0.2, shuffle=True, random_state=42)
        
    
    move_path = 'YOLO_dataset'
    if(os.path.exists(move_path)):
        print(f'[*] Already exists')
        exit(0)
    os.makedirs(os.path.join(move_path, "images/train"))
    os.makedirs(os.path.join(move_path, "images/val"))
    os.makedirs(os.path.join(move_path, "labels/train"))
    os.makedirs(os.path.join(move_path, "labels/val"))
    
    ## flame train images
    for X, y in tqdm(zip(flame_X_train, flame_y_train), desc=f'flame train move.....'):
        X_name, y_name = X.split('\\')[-1], y.split('\\')[-1]
        
        shutil.copyfile(X, os.path.join(move_path, "images/train", X_name))
        shutil.copyfile(y, os.path.join(move_path, "labels/train", y_name))
        
    ## flame val images
    for X, y in tqdm(zip(flame_X_val, flame_y_val), desc=f'flame val move.....'):
        X_name, y_name = X.split('\\')[-1], y.split('\\')[-1]
        
        shutil.copyfile(X, os.path.join(move_path, "images/val", X_name))
        shutil.copyfile(y, os.path.join(move_path, "labels/val", y_name))
        
    ## smoke train images
    for X, y in tqdm(zip(smoke_X_train, smoke_y_train), desc=f'smoke train move.....'):
        X_name, y_name = X.split('\\')[-1], y.split('\\')[-1]
        
        shutil.copyfile(X, os.path.join(move_path, "images/train", X_name))
        shutil.copyfile(y, os.path.join(move_path, "labels/train", y_name))
        
    ## smoke val images
    for X, y in tqdm(zip(smoke_X_val, smoke_y_val), desc=f'smoke val move.....'):
        X_name, y_name = X.split('\\')[-1], y.split('\\')[-1]
        
        shutil.copyfile(X, os.path.join(move_path, "images/val", X_name))
        shutil.copyfile(y, os.path.join(move_path, "labels/val", y_name))