import streamlit as st
from util import item03_util as item03
import os
from PIL import Image


script_dir = os.path.dirname(__file__)
pic_dict = {}
for i in range(4,9):
    pic_dict[f'item{i}'] = Image.open(script_dir + f'\\\\images\\\\item{i}.png')

text_line_강예진 = '''
                    **강예진 [INFP]**\n
                    **1.** 데이터 수집\n
                    **2.** 모델링\n
                    **3.** 챗봇 제작
                    '''
caption_강예진 = '강예진 [INFP]'
    

text_line_김영훈 = '''
                    **김영훈 [INTP]**\n
                    **1.** 데이터 수집\n
                    **2.** 시각화\n
                    **3.** 프로젝트 다이어그램 제작
                    '''
caption_김영훈 = '김영훈 [INTP]'
    

text_line_윤다정 = '''
                    **윤다정 [ISTP]**\n
                    **1.** 데이터 수집\n
                    **2.** 데이터 전처리\n
                    **3.** 시각화
                    '''
caption_윤다정 = '윤다정 [ISTP]'
    

text_line_이정욱 = '''
                    **이정욱 [ENFJ]**\n
                    **1.** 데이터 수집\n
                    **2.** 데이터 전처리\n
                    **3.** streamlit 표출
                    '''
caption_이정욱 = '이정욱 [ENFJ]'
    

text_line_정은주 = '''
                    **정은주 [INFJ]**\n
                    **1.** 모델링\n
                    **2.** PPT 제작\n
                    **3.** 발표
                    '''
caption_정은주 = '정은주 [INFJ]'



def app():  
    item03.item03_title()
    item03.item03_desc01(pic_dict['item4'], text_line_강예진, caption_강예진)
    item03.item03_desc01(pic_dict['item5'], text_line_김영훈, caption_김영훈)
    item03.item03_desc01(pic_dict['item6'], text_line_윤다정, caption_윤다정)
    item03.item03_desc01(pic_dict['item7'], text_line_이정욱, caption_이정욱)
    item03.item03_desc01(pic_dict['item8'], text_line_정은주, caption_정은주)