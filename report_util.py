import streamlit as st
import os
import os.path as osp
import uuid
import requests
import json
import olefile
from shutil import copyfile

def save_uploadedfile(uploadedfile):
    os.makedirs("temp", exist_ok=True)
    
    fname = str(uuid.uuid4()) + '.mp4'
    
    with open(osp.join("temp", fname), "wb") as f:
        f.write(uploadedfile)

    return fname


def get_location():
    send_url = "[MY-API-KEYS]"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    
    return latitude, longitude

def save(data):
    os.makedirs("report_video", exist_ok=True)
    
    for f in os.listdir('temp'):
        p = osp.join('temp', f)
        copyfile(p, osp.join('report_video', f))
        
        
def remove_all():
    for f in os.listdir('temp'):
        p = osp.join('temp', f)
        
        os.remove(p)