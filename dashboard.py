import streamlit as st
from report_util import *
import os
import os.path as osp
import pandas as pd
   
   
st.title("Wildfire Dashboard")
st.markdown("Authored by : [Lupin](https://github.com/devLupin)")
st.markdown("")
st.markdown("")

users_prefix = 'process_video'
if osp.isdir(users_prefix) == False or len(os.listdir(users_prefix)) == 0:
    st.markdown("### Empty video")
    st.stop()

users = os.listdir(users_prefix)

tabs = st.tabs([user for user in users])

for i, tab in enumerate(tabs):
    with tab:
        
        user = osp.join(users_prefix, users[i])
        videos = os.listdir(user)
        
        for f in videos:
            
            if f.split('.')[-1] == 'txt':
                continue
            
            cur = osp.join(user, f)
            file = open(cur, 'rb')
            v_bytes = file.read()
            file.close()
            
            txt = f.split('.')[0] + '.txt'
            f = open(osp.join(user, txt), 'r')
            info = f.readlines()[0].split(' ')
            
            st.markdown("")
            st.markdown(f'###### Date : {info[0]} {info[1]}')
            
            ## Create a sample DataFrame with latitude and longitude values
            data = pd.DataFrame({
                'latitude': [float(info[2])],
                'longitude': [float(info[3])]
            })
            
            st.video(v_bytes)
            
            st.markdown("")
            st.markdown(f'###### User Location')
            
            ## Create a map with the data
            st.map(data, zoom=14)