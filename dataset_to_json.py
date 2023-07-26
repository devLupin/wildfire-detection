import os
from natsort import natsorted
import csv
from tqdm import tqdm

root_path = "dataset"
image_path = os.path.join(root_path, "images")
label_path = os.path.join(root_path, "labels")
classes = os.listdir(image_path)

if __name__ == '__main__':
    save_path = 'dataset/data.csv'
    
    if(os.path.exists(save_path)):
        print(f'[*] Already exists')
        exit(0)
    
    f = open(save_path, 'w', newline='')
    wr = csv.writer(f)
    
    for c in classes:
        cur_c_image = os.path.join(image_path, c)
        cur_c_label = os.path.join(label_path, c)
        
        # order by character
        image_list = os.listdir(cur_c_image)
        image_list = natsorted(image_list)
        label_list = os.listdir(cur_c_label)
        label_list = natsorted(label_list)
        
        for i in tqdm(range(len(image_list)), f'current dir : {image_path}/{c}'):
            c_label_path = os.path.join(cur_c_label, label_list[i])
            tmp = open(c_label_path, mode="r")
            line = tmp.read()
            c_pos = line.split(' ')[1:]
            c_image_path = os.path.join(cur_c_image, image_list[i])
            wr.writerow([c, c_image_path, c_pos[0], c_pos[1], c_pos[2], c_pos[3][:-1]])
            