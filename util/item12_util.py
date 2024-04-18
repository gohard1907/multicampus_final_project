import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image

script_dir = os.path.dirname(__file__)
pic_dict = {}
for i in range(34, 35):
    pic_dict[f'item{i}'] = Image.open(script_dir + f'\\\\images\\\\item{i}.png')


def item12_title():
    st.title('개발 후기 및 느낀 점')
    #st.header('페이지에 관한 개괄적 설명')
    #st.write('''본문''')



def item12_desc01():
    st.header('')
    #st.image(pic_dict['item35'],
             #use_column_width=True)
    st.write('''
             **1.** 주제에 맞는 데이터 수집이 어렵다.\n
             **2.** EDA 과정을 조금 더 깊게 진행했다면 분석 과정에서의 시간이 단축됐을 것 같다.\n
             **3.** 6개월 간 배운 내용을 모두 적용해볼 수 있어서 좋았다.\n
             **4.** 모델 정확도를 올리는 과정에서 데이터 복제, 증폭 등 실무에서의 활용 방법을 경험해볼 수 있었다.\n
             **5.** 데이터가 커질수록 모델 적용이 오래 걸려서 다양한 모델 적용과 최적의 파라미터 찾기에 시간이 부족한 게 아쉬웠다.\n
             **6.** 시각화 방법이나 모델링보다 데이터 수집과 전처리가 더 중요하다는 것을 깨달았다.\n
             ''')