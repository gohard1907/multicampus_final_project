import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image

script_dir = os.path.dirname(__file__)
pic_dict = {}
for i in range(30, 34):
    pic_dict[f'item{i}'] = Image.open(script_dir + f'\\\\images\\\\item{i}.png')



def item11_title():
    st.title('기대효과 및 한계와 개선 방향')
    #st.header('페이지에 관한 개괄적 설명')
    #st.write('''본문''')



def item11_desc01():
    st.header('1. 기대효과')
    st.image(pic_dict['item30'],
             use_column_width=True)
    st.write('''
             
             ''')
    st.image(pic_dict['item31'],
             use_column_width=True)
    st.write('''
             
             ''')
    st.image(pic_dict['item32'],
             use_column_width=True)
    st.write('''
             
             ''')
    st.header('')
    
    st.header('2. 한계 및 개선방향')
    st.image(pic_dict['item33'],
             use_column_width=True)