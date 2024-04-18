import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from PIL import Image


script_dir = os.path.dirname(__file__)
pic_dict = {}
for i in range(2,4):
    pic_dict[f'item{i}'] = Image.open(script_dir + f'\\\\images\\\\item{i}.png')


def item02_title():
    st.title('MBTI 소개')
    #st.header('MBTI란?')
    #st.write('''본문''')
    


def item02_desc01():
    st.header('MBTI란?')
 
    st.image(pic_dict['item2'], caption='[그림 2-1] 16가지 MBTI', use_column_width=True)
    st.write('''
             MBTI(Myers-Briggs Type Indicator)는 개인이 쉽게 응답할 수 있는 자기보고서 문항을 통해 파악하는 개인의 선호 경향입니다.
             각자 선호하는 심리 경향들이 인간의 행동에 어떠한 영향을 미치는가를 파악하여 실생활에 응용할 수 있도록 제작된 심리 검사입니다.
             ''')
             
    st.write('')
    
    st.image(pic_dict['item3'], caption='[그림 2-2] MBTI 판단 척도', use_column_width=True)
    st.write('''
             위와 같이 여덟 가지의 척도로 나뉘며, 네 가지 척도의 조합을 통해 총 16가지 MBTI를 도출할 수 있습니다. 
             ''')
    st.write('')
    st.write('')
             
    st.header('각 척도에 대한 예시')
    st.write('')
    st.write('''
             **"친구와 만나기로 했는데 갑자기 약속이 취소되었을 때"**\n
             I: 갑자기 혼자만의 시간이 생겼잖아? 뭐하지? 너무 편하다~\n
             E: 아.. 이럴수가... 그럼 누굴 대신 만나지? 전화해봐야겠다.\n
             
             **"비행기 타기 전에 무슨 생각해?"**\n
             N: 비행기가 추락하면 어쩌지? 비상구 자리에 앉아야 하나? (상상력 풍부)\n
             S: 기내식 뭐 나오지? 가는 동안 영화나 볼까? (현실에 관련된 생각)\n
             
             **"나 교통사고 났어"**\n
             F: 어머! 많이 다쳤어? 괜찮아? (공감과 걱정 먼저)\n
             T: 보험은 들어놨어? 누구 과실이야? (해결방안 제시)\n
             
             **"여행은 어떻게 할까?"**\n
             J: 9시에 출발해서 여기서 밥먹고 거기 들려서 이렇게 저렇게 놀자! (계획적)\n
             P: 일단 밥 먹고 나머지는 가면서 생각해볼까? (즉흥적)
             ''')