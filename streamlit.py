import streamlit as st

#Title
st.title("Title")

#Header
st.header("Header")

#SubHeader
st.Subheader("Subheader")

# Make text
st.write("Hello World")

#cache
import streamlit as st
'''
데이터가 많을 때 중간에 캐쉬를 놓아서 속도를 개선시킨다.
1. 함수 이름 확인
2. 함수를 구성하는 코드 확인
3. 함수 호출시 사용한 매개변수
4. 위 3개를 로컬에 저장해두고 가시 호출시 사용할 수 있으면 그대로 사용한다
'''
#데코레이션, 함수를 꾸밈
#함수에서 반복적으로 사용되는 것들을 모아 놓은 것
@st.cache
def load_data():
    #load data
    pass
streamlit run streamlit.py