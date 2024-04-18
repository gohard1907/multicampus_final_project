import streamlit as st

from app_multipage import Multipage
from page import item01, item02, item03, item04, item05, item06, item07, item08, item09, item10, item11, item12

# Instance creation for the app
app = Multipage()

# Title of the main page
#st.title('MBTI별 곡 추천')

# Add applications
app.add_page("1. 프로젝트 기획 배경 및 목표", item01.app)
app.add_page("2. MBTI 소개", item02.app)
app.add_page("3. 구성원 및 역할", item03.app)
app.add_page("4. 프로젝트 다이어그램", item04.app)
app.add_page("5. 데이터 수집 & 소개", item05.app)
app.add_page("6. 데이터 전처리", item06.app)
app.add_page("7. EDA", item07.app)
app.add_page("8. 모델링", item08.app)
app.add_page("9. 결과 출력", item09.app)
app.add_page("10. 챗봇", item09.app)
app.add_page("11. 기대효과 및 한계", item10.app)
app.add_page("12. 개선 방향", item11.app)

app.run()