import streamlit as st
from page import item01 as item01
from page import item02 as item02
from page import item03 as item03
from page import item04 as item04
from page import item05 as item05
from page import item06 as item06
from page import item07 as item07
from page import item08 as item08
from page import item09 as item09
from page import item10 as item10
from page import item11 as item11
from page import item12 as item12

#st.title('Project')

item_list = ['item01', 'item02', 'item03', 'item04', 'item05', 
             'item06', 'item07', 'item08', 'item09', 'item10', 
             'item11', 'item12']

item_labels = {
'item01':'01. 프로젝트 기획 배경 및 목표', 'item02':'02. MBTI 소개', 
'item03':'03. 구성원 및 역할', 'item04':'04. 프로젝트 다이어그램', 
'item05':'05. 데이터 수집 & 소개', 'item06':'06. 데이터 전처리',
'item07':'07. EDA', 'item08':'08. 모델링', 'item09':'09. 결과 시연',
'item10':'10. 챗봇', 'item11':'11. 기대효과 및 한계',
'item12':'12. 개발 후기 및 느낀 점', 
}

FIL = lambda x : item_labels[x]
item = st.sidebar.selectbox('항목을 고르세요.',  item_list, format_func = FIL )

if item == 'item01':
	item01.app()
elif item == 'item02':
	item02.app()
elif item == 'item03':
	item03.app()
elif item == 'item04':
	item04.app()
elif item == 'item05':
	item05.app()
elif item == 'item06':
	item06.app()
elif item == 'item07':
	item07.app()
elif item == 'item08':
	item08.app()
elif item == 'item09':
	item09.app()
elif item == 'item10':
	item10.app()
elif item == 'item11':
	item11.app()
elif item == 'item12':
	item12.app()
