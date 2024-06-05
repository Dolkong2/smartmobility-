import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
from PIL import Image # pandas에서 사진을 올리는데 필요한 모듈
st.write('hello world')
st.info('This is a purely informational message', icon="ℹ️") # info boc
st.warning('This is a warning', icon="⚠️") # warning box
st.success('This is a success message!', icon="✅") #success box
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')  # spinner box
#st.balloons() # balloon box
#st.snow()
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

st.image('original.jpg', caption='flowers by the mountains') # image 
picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)