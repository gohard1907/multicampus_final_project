import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image

script_dir = os.path.dirname(__file__)
pic_dict = {}
for i in range(21, 29):
    pic_dict[f'item{i}'] = Image.open(script_dir + f'\\\\images\\\\item{i}.png')


def item08_title():
    st.title('모델링')
    #st.header('페이지에 관한 개괄적 설명')
    #st.write('''본문''')



def item08_desc01():
    st.header('1. 초기 모델링')
    st.image(pic_dict['item21'],
             caption='[그림 8-1] 프로젝트 수행에 사용한 모델들',
             use_column_width=True)
    st.write('''
             MBTI별 선호하는 음원 특성과 신곡 음원 특성의 유사도를 비교하였으나 특성의 평균값에 큰 차이가 없어서 유의미한 결과를 도출하지 못 했다.
             ''')
             
             
    st.header('2. 데이터 학습 후 MBTI 선호곡 추천')
    st.image(pic_dict['item22'],
             caption='[그림 8-2] XGBoost 예시',
             use_column_width=True)
    #st.write('''
             
             #''')
             
             
    st.header('3. 각 특성별 t검정')
    st.image(pic_dict['item23'],
             caption='[그림 8-3] 각 지표별 t검정 결과',
             use_column_width=True)
    st.write('''
             1. 각각의 데이터가 17,000개 이상이므로 중심극한정리에 따라 정규성을 따른다고 가정한다.
             2. Levene의 등분산 검정으로 등분산성 가정/등분산 가정이 만족하지 않을 경우 Welch t 검정을 진행하였다.
             3. MBTI 성향이 E이면서 I일 수 없고, N이면서 S일 수 없으니 각 그룹이 서로 독립적이라고 가정하였다.
             ''')
             
             
    st.header('4. MBTI 지표별 세분화 후 데이터 통합')
    st.image(pic_dict['item24'],
             caption='[그림 8-4] MBTI 지표별 세분화 후 데이터 통합')
    #st.write('''
             
             #''')
             
             
    st.header('5. Voting Classifier 사용')
    st.image(pic_dict['item25'],
             caption='[그림 8-5] Voting Classifier 사용')
    #st.write('''
             
             #''')
             
             
    st.header('6. Feature값을 미세 조정한 데이터를 복제 및 증폭')
    st.image(pic_dict['item26'],
             caption='[그림 8-6] 데이터 복제')
    st.image(pic_dict['item27'],
             caption='[그림 8-7] 데이터 증폭')
    #st.write('''
             
             #''')
             
             
    st.header('7. 최종 모델')
    st.image(pic_dict['item28'],
             caption='[그림 8-8] 최종 모델 및 정확도')
    st.write('''
             상기 과정을 거쳐 최종적으로 정확도를 64.1%까지 향상시킬 수 있었다.
             ''')