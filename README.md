# 파이썬
python Version

모든 코드는 python version 3.8로 작성하였습니다.

- setting

file -> settings -> python interpreter -> streamlit install

- streamlit 사용

streamlit import streamlit as st

- 제목 출력

<img width="551" alt="제목" src="https://user-images.githubusercontent.com/81000484/156863297-e8b9f5c7-4e8d-4074-9d86-f6327aa0a958.png">

st.header("독서와 성적의 상관관계")

st.subheader("----------------------------------------------------------------------")

- radio(옵션선택 1)

사진

st.write("1. 성별 ")
a = st.radio ("성별을 골라주세요.", ("남", "여"))

- text_input(답변입력)

사진

st.write("2-1. 내신등급 ")

b = st.text_input("소수점 첫째 자리까지 입력해주세요.")
