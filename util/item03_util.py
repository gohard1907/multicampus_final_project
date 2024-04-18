import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



def item03_title():
    st.title('구성원 및 역할')
    #st.header('페이지에 관한 개괄적 설명')
    #st.write('''본문''')



def item03_desc01(image_path, text_line, caption):
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(image_path, caption=caption, use_column_width=True)
    with col2:
        st.write(text_line)