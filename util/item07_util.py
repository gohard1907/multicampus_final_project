import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image


script_dir = os.path.dirname(__file__)
pic_dict = {}
for i in range(14, 21):
    pic_dict[f'item{i}'] = Image.open(script_dir + f'\\\\images\\\\item{i}.png')


def item07_title():
    st.title('EDA')
    #st.header('페이지에 관한 개괄적 설명')
    #st.write('''본문''')



def item07_desc01():
    
    st.header('1. 음악의 여섯 가지 특성에 대한 선호도 그래프')
    st.image(pic_dict['item14'], 
             caption='[그림 7-1] 선호도 그래프 1', 
             use_column_width=True)
    st.image(pic_dict['item15'], 
             caption='[그림 7-2] 선호도 그래프 2', 
             use_column_width=True)
    st.header('')
    st.header('')
             
    
    
    st.header('2. Instrumentalness와 Acousticness에 대한 MBTI 지표별 선호도')
    st.image(pic_dict['item16'],
             caption='[그림 7-3] MBTI 지표별 선호도',
             use_column_width=True)
    st.header('')
    st.header('')
             
             
             
    st.header('3. MBTI 유형별 선호 특성에 대한 산점도 그래프')
    st.image(pic_dict['item17'],
             caption='[그림 7-4] MBTI 유형별 Danceability와 Energy 선호도',
             use_column_width=True)
    st.image(pic_dict['item18'],
             caption='[그림 7-5] MBTI 유형별 Acousticness와 Instrumentalness 선호도',
             use_column_width=True)
    st.image(pic_dict['item19'],
             caption='[그림 7-6] MBTI 유형별 Speechiness와 Loudness 선호도',
             use_column_width=True)
    st.write('''
             **위 그래프들을 통해 상반된 MBTI 지표 간에 선호하는 음악적 특성에 차이가 있음을 볼 수 있다.**
             ''')
    st.header('')
    
             
    
    #st.header('4. T 검정 분석')
    #st.image(pic_dict['item20'],
             #caption='[그림 7-7] 각 지표별 t검정 결과',
             #use_column_width=True)
    #st.write('''
             #1. 각각의 데이터가 17,000개 이상이므로 중심극한정리에 따라 정규성을 따른다고 가정한다.
             #2. Levene의 등분산 검정으로 등분산성 가정/등분산 가정이 만족하지 않을 경우 Welch t 검정을 진행하였다.
             #3. MBTI 성향이 E이면서 I일 수 없고, N이면서 S일 수 없으니 각 그룹이 서로 독립적이라고 가정하였다.
             #''')