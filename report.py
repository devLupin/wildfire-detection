import streamlit as st
from st_pages import Page, show_pages, add_page_title
from report_util import *
import pandas as pd
from shutil import copyfile


st.title("Wildfire Reporting for Mobile")
st.markdown("Authored by : [Lupin](https://github.com/devLupin)")

st.markdown("")
st.markdown("")


phnum = st.text_input('Input your phone number(ex. 010-1234-5678)', '')
start_btn = st.button('☑ Confirm')
if phnum == '':
    st.stop()

st.markdown("")
st.markdown("")



uploaded_file = st.file_uploader("Record/Choose a wildfire video file", accept_multiple_files=False)

if uploaded_file is None:
    st.stop()
    
bytes_data = uploaded_file.read()
fname = save_uploadedfile(bytes_data, phnum)

st.markdown("")
st.markdown("")

        
with st.form("temp", clear_on_submit=True):
    st.markdown("")
    st.markdown("### ⏩ Check your video")
    

    f_name = osp.join('user', phnum, fname)
    video_file = open(f_name, 'rb')
    video_bytes = video_file.read();
    video_file.close()
    
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
    
    
    if st.form_submit_button("✅ Submit"):
        st.markdown("## **Your submission is complete.**")
        st.markdown("## **Please close this page.**")
        save(phnum)
    
    else:
        st.stop()