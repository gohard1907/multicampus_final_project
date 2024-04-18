import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image

script_dir = os.path.dirname(__file__)
pic_dict = {}
for i in range(1,2):
    pic_dict[f'item{i}'] = Image.open(script_dir + f'\\\\images\\\\item{i}.png')


#def item01_title():
    #st.title('음원 데이터 분석을 통한 MBTI 예측 및 성향에 맞는 신곡 추천')
    #st.header('페이지에 관한 개괄적 설명')
    #st.write('''본문''')



def item01_desc01():
 
    st.image(pic_dict['item1'], use_column_width=True)
    st.header('프로젝트 기획 배경')
    st.write('''
             새로운 음악은 듣고 싶지만 매일 쏟아지는 신곡 릴레이에 지친 사용자를 위해
             MBTI를 기반으로 사용자의 취향에 맞는 곡을 추천해주는 음악 큐레이팅 서비스입니다.
             ''')