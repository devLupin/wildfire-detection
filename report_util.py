import streamlit as st
import os
import os.path as osp
import uuid
import requests
import json
from shutil import copyfile, rmtree
from Config import Config

def save_uploadedfile(uploadedfile, phnum):
    os.makedirs(osp.join('user', phnum), exist_ok=True)
    
    fname = str(uuid.uuid4()) + '.mp4'
    
    with open(osp.join('user', phnum, fname), "wb") as f:
        f.write(uploadedfile)

    return fname


def get_location():
    send_url = f'http://api.ipstack.com/check?access_key={Config.LOCATION_API}'
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    
    return latitude, longitude


def save(phnum):
    tmp_dir = osp.join('user', phnum)
    save_dir = osp.join('record_video', phnum)
    os.makedirs(save_dir, exist_ok=True)
    
    li = os.listdir(tmp_dir)
    
    if len(li) == 0:
        return
    
    copyfile(osp.join(tmp_dir, li[0]), osp.join(save_dir, li[0]))
    remove(phnum)
    
    
def save_info(phnum, fname):
    from datetime import datetime
    now = datetime.now()
    latitude, longitude = get_location()
    
    save_dir = osp.join('process_video', phnum)
    os.makedirs(save_dir, exist_ok=True)
    
    f = open(osp.join(save_dir, fname.split('.')[0]+'.txt'), 'w+')
    f.write(now.strftime('%Y-%m-%d %H:%M:%S') + ' ' + str(latitude) + ' ' + str(longitude))
    f.close()
    
    
def remove(phnum):
    cur_dir = osp.join('user', phnum)
    rmtree(cur_dir)
    
