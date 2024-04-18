import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image

script_dir = os.path.dirname(__file__)
pic_dict = {}
for i in range(9,10):
    pic_dict[f'item{i}'] = Image.open(script_dir + f'\\\\images\\\\item{i}.png')


def item04_title():
    st.title('프로젝트 다이어그램')
    #st.header('페이지에 관한 개괄적 설명')
    #st.write('''본문''')



def item04_desc01():

    st.image(pic_dict['item9'], caption='[그림 4-1 프로젝트 다이어그램]', use_column_width=True)