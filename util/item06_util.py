import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image

script_dir = os.path.dirname(__file__)
pic_dict = {}
for i in range(13,14):
    pic_dict[f'item{i}'] = Image.open(script_dir + f'\\\\images\\\\item{i}.png')

def item06_title():
    st.title('데이터 전처리')
    #st.header('페이지에 관한 개괄적 설명')
    #st.write('''본문''')



def item06_desc01():
    st.header('데이터 전처리 기준')
    st.image(pic_dict['item13'],
             caption='[그림 6-1] (예시) 무작위로 입력한 플레이리스트 제목에 MBTI 유형이 포함된 경우 삭제')
    st.write('''
             1. 플레이리스트 제목에 MBTI와 관련 없는 내용이 들어갈 경우 데이터를 삭제하였습니다.\n
             2. 동일 플레이리스트 내의 중복곡들은 삭제 처리하고, 한 번만 출력되도록 수정하였습니다.\n
             3. MBTI 특성별로 전체 곡 수가 상이해 Oversampling을 진행하였습니다.\n
             4. Key값을 더미화하여 진행하였습니다.\n
             5. 전처리를 거친 각 MBTI 유형별 플레이리스트들을 병합하여 하나의 csv파일로 저장 및 분석하였습니다.
             ''')