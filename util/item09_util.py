import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from streamlit import session_state
import os


def item09_title():
    st.title('결과 시연')
    #st.header('페이지에 관한 개괄적 설명')
    #st.write('''본문''')
    
    

def item09_desc02():
    st.header('신곡 추천 프로그램')
    data_path = os.path.dirname(__file__) + "\\images\\item29_new_released_list.csv"
    data_df = pd.read_csv(data_path)

    # session_state를 사용하여 이전에 선택한 곡들을 저장
    if not hasattr(session_state, "selected_songs"):
        session_state.selected_songs = pd.DataFrame(columns=['mbti', 'Track Name', 'Artists'])

    user_mbti = st.text_input('MBTI를 입력하세요 (예: ENFJ)')

    # 사용자가 엔터를 눌렀을 때 이벤트 감지
    if st.button('Enter', key="enter_button"):
        # 데이터프레임에서 조건을 만족하는 행의 개수를 확인
        num_rows_satisfying_condition = len(data_df[data_df['mbti'] == user_mbti])

        # 충분한 행이 있을 경우에만 sample 함수 호출
        if num_rows_satisfying_condition >= 3:
            selected_rows = data_df[data_df['mbti'] == user_mbti].sample(n=3)

            # 결과 테이블 출력
            st.table(selected_rows[['mbti', 'Track Name', 'Artists']])

            # "들으러 가기" 버튼 생성
            URL_STRING = "https://open.spotify.com/?"
            st.markdown(
    f'<a href="{URL_STRING}" style="display: inline-block; padding: 12px 20px; background-color: #4CAF50; color: white; text-align: center; text-decoration: none; font-size: 16px; border-radius: 4px;">Listen on Spotify</a>',
    unsafe_allow_html=True
)
            
        
        
def item09_desc03():
    st.header('신곡 추천 프로그램')
    data = os.path.dirname(__file__) + "\\images\\item29_new_released_list.csv"
    data_df = pd.read_csv(data)
    mbti_options = data_df['mbti'].unique()
    
    # MBTI 선택 드롭박스, 초기값은 "mbti를 선택하세요."
    user_mbti = st.selectbox('', ['MBTI를 선택하세요.'] + list(mbti_options))
    
    # 초기값이 "mbti를 선택하세요."인 경우 결과 테이블 출력하지 않음
    if user_mbti != 'mbti를 선택하세요.':
        num_rows_satisfying_condition = len(data_df[data_df['mbti'] == user_mbti])
        if num_rows_satisfying_condition >= 3:
            # 선택된 MBTI에 대한 무작위 3곡 추천
            selected_rows = data_df[data_df['mbti'] == user_mbti].sample(n=3)
            
            # 결과 테이블 출력
            st.write(f'{user_mbti}를 위한 추천곡입니다.')
            st.table(selected_rows[['mbti', 'Track Name', 'Artists']])
            
            # "들으러 가기" 버튼 스타일 설정
            button_style = (
                "display: block;"
                "margin: 0 auto;"
                "padding: 12px 4px;"
                "background-color: #4CAF50;"
                "color: white;"
                "text-align: center;"
                "text-decoration: none;"
                "font-size: 16px;"
                "border-radius: 4px;"
            )
            
            # "들으러 가기" 버튼 링크 생성
            URL_STRING = "https://open.spotify.com/?"
            st.markdown(
                f'<div style="{button_style}">'
                f'<a href="{URL_STRING}" style="color: white; text-decoration: none;">Listen on Spotify</a>'
                '</div>',
                unsafe_allow_html=True
            )
