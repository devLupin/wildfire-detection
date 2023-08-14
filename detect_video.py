import os
import os.path as osp
import cv2
from natsort import natsorted
from ultralytics import YOLO
from Config import Config
import moviepy.video.io.ImageSequenceClip
from shutil import rmtree
from time import sleep


def video2frame(cur_video):
    save_path = 'video2frame'
    os.makedirs(save_path, exist_ok=True)
    
    vidcap = cv2.VideoCapture(cur_video)
    success,image = vidcap.read()
    count = 0
    while success:
      cv2.imwrite(f"{save_path}/%06d.jpg" % count, image)     # save frame as JPEG file
      success,image = vidcap.read()
      if success is False:
        continue

      count += 1
      
    return save_path
    
    
def detect_frame(path):
    save_path = 'detect_frame'
    os.makedirs(save_path, exist_ok=True)
    
    model = YOLO(Config.MODEL)
    blue_color = (255, 0, 0)
    
    origin = os.listdir(path)
    origin = natsorted(origin) ## order by desc
    
    count = 0
    
    for f in origin:
        img = cv2.imread(osp.join(path, f))

        results = model.predict(img)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                b = box.xyxy[0]
                c = box.cls

                x1, y1, x2, y2 = int(b[0]), int(b[1]), int(b[2]), int(b[3])

                img = cv2.rectangle(img, (x1, y1), (x2, y2), blue_color, 3)
                img = cv2.putText(
                    img,
                     "Fire" if c == 1 else "Smoke",
                    (x1, y1 - 15 if y1 - 15 > 15 else y1 + 15),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    blue_color,
                    2,
                )

        cv2.imwrite(f"{save_path}/%06d.jpg" % count, img)
        count += 1
        
    return save_path
    
    


def processing_video():
    save_prefix = 'process_video'
    root_prefix = 'record_video'
    
    if not osp.isdir(root_prefix):
        return
    
    users = os.listdir(root_prefix)
    
    os.makedirs(save_prefix, exist_ok=True)
    
    for user in users:
        save_prefix = osp.join(save_prefix, user)
        os.makedirs(save_prefix, exist_ok=True)
        
        user_prefix = osp.join(root_prefix, user)
        for f in os.listdir(user_prefix):
            cur_video = osp.join(user_prefix, f)
            
            frame_path = video2frame(cur_video)
            detect_path = detect_frame(frame_path)

            image_files = os.listdir(detect_path)
            image_files = natsorted(image_files)
            image_files = [osp.join(detect_path, img) for img in image_files]

            clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=30)
            clip.write_videofile(osp.join(save_prefix, f.split('.')[0] + '.mp4'))
            
            rmtree(frame_path)
            rmtree(detect_path)
            
        rmtree(user_prefix)
            
            
            

if __name__ == '__main__':
    while(sleep(5000)):
        processing_video()