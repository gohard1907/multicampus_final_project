import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image

script_dir = os.path.dirname(__file__)
pic_dict = {}
for i in range(11,13):
    pic_dict[f'item{i}'] = Image.open(script_dir + f'\\\\images\\\\item{i}.png')

data_features = {'특성':['Danceability', 'Energy', 'Key', 'Loudness', 'Mode',
                           'Speechiness', 'Acousticness', 'Instrumentalness',
                           'Liveness', 'Valence', 'Tempo', 'Time Signature'],
                     '설명':['춤추기 알맞은 곡인지 알려주는 척도, 값이 높을수록 춤추기 좋다.' , 
                           '에너지 수준, 값이 높을수록 활기찬 곡이다.' ,
                           '음계를 의미하며, 0부터 11까지 존재하고 C부터 B#까지 표현한다.' ,
                           '전체적인 음량을 의미하며, 범위는 -60에서 0까지이다.' ,
                           '조성을 의미하며 0은 단조, 1은 장조이다.' ,
                           '곡 내에서 말의 정도이며, 값이 높을수록 인간의 음성이 많음을 의미한다.' ,
                           '전자적이지 않은 음향의 정도를 의미하며 값이 높을수록 비 전자적인 악기의 비중이 높음을 의미한다.' ,
                           '악기의 비중을 의미하며, 값이 높을수록 보컬보다 악기의 비중이 높은 음악이다.' ,
                           '라이브 정도를 의미하며, 값이 높을수록 라이브 음악의 특성을 띈다.' ,
                           '감정 수준을 의미하며, 값이 높을수록 긍정적 감정을 가진 음악이다.' ,
                           'BPM으로 통용되는 속도를 의미하며, 값이 높을수록 빠른 음악이다.' ,
                           '박자 표시이며 범위는 3 ~ 7을 사용한다.']}
df_data_features = pd.DataFrame(data_features)

def item05_title():
    st.title('데이터 수집 & 소개')



def item05_desc01():   
    st.header('1. Spotify API 활용')
    st.image(pic_dict['item11'], 
             caption='[그림 5-1] API를 활용할 수 있도록 Spotify 자체에서 개발자를 위해 제공하는 개발자 사이트', 
             use_column_width=True)
    st.write('')
    
    st.header('2. MBTI 유형별 플레이리스트 검색')
    st.image(pic_dict['item12'],
             caption='[그림 5-2] (예시) INFP 플레이리스트 검색 결과',
             use_column_width=True)
    st.write('')
    st.write('''
             1. 각 MBTI 유형별로 플레이리스트를 검색하였습니다.\n
             2. 유형별로 플레이리스트를 30개씩 추출하였습니다.
                 이 때, 플레이리스트는 인기순으로 내림차순 정렬하여 상위 30개를 사용하였습니다.\n
             3. 플레이리스트별로 약 100곡씩 추출하여 MBTI 유형별로 3,000곡의 음원 정보를 저장하였습니다.\n
             4. 총합 약 50,000곡으로 작업하였습니다.
             ''')
    st.write('')
             
    st.header('3. 음원 특성 및 정보 유형')
    st.table(df_data_features)