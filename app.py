import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
from ultralytics import YOLO
import os
import pandas as pd
from Config import Config

clear = lambda: os.system('cls')

# Load model
model = YOLO(Config.MODEL)
blue_color = (255, 0, 0)

st.title("Real-tim Fire Detection")
st.markdown("Authored by : [Lupin](https://github.com/devLupin)")


def callback(frame):
    clear()
    img = frame.to_ndarray(format="bgr24")
    img = detect(img)

    return av.VideoFrame.from_ndarray(img, format="bgr24")

def detect(img):
    
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
                "Fire",
                (x1, y1 - 15 if y1 - 15 > 15 else y1 + 15),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                blue_color,
                2,
            )
            
    return img


webrtc_streamer(key="example", video_frame_callback=callback)

