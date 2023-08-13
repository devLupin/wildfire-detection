import streamlit as st
from report_util import *
import pandas as pd

remove_all()

st.title("Wildfire Reporting")
st.markdown("Made by [Lupin](https://github.com/devLupin)")

st.markdown("")
st.markdown("")

uploaded_files = st.file_uploader("Record/Choose a wildfire video file", accept_multiple_files=True)

data = []
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    fname = save_uploadedfile(bytes_data)
    data.append(fname)
    
if len(data) == 0:
        st.stop()
        
st.markdown("")
st.markdown("")

        
with st.form("temp", clear_on_submit=True):
    st.markdown("")
    st.markdown("### ⏩ Check your video")
    
    for f in data:
        f_name = osp.join('temp', f)
        video_file = open(f_name, 'rb')
        video_bytes = video_file.read();
        
        st.video(video_bytes)
    
    
    
    st.markdown("")
    st.markdown("### 👀 Check your location")
    
    latitude, longitude = get_location()
 
    ## Create a sample DataFrame with latitude and longitude values
    data = pd.DataFrame({
        'latitude': [latitude],
        'longitude': [longitude]
    })
    
    ## Create a map with the data
    st.map(data, zoom=14)
    
    submit_btn = st.form_submit_button("✅ Submit")
    