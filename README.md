# streamlit <form>
- python Version

  python version 3.8

- setting

  file -> settings -> python interpreter -> streamlit install

- streamlit 사용

  streamlit import streamlit as st

- 제목 출력

  <img width="551" alt="제목" src="https://user-images.githubusercontent.com/81000484/156863297-e8b9f5c7-4e8d-4074-9d86-f6327aa0a958.png">

  st.header("독서와 성적의 상관관계")

  st.subheader("----------------------------------------------------------------------")

- radio(옵션선택 1)

  <img width="558" alt="1번" src="https://user-images.githubusercontent.com/81000484/156864062-f01872fa-6733-482c-ab17-6262384e461b.png">

  st.write("1. 성별 ")
  a = st.radio ("성별을 골라주세요.", ("남", "여"))

- text_input(답변입력)

  <img width="552" alt="내신등급" src="https://user-images.githubusercontent.com/81000484/156864097-b1045f11-ee5f-4e50-aeb1-f5a136f7376c.png">

  st.write("2-1. 내신등급 ")

  b = st.text_input("소수점 첫째 자리까지 입력해주세요.")
  
- text_area(길거나 많은 답변 입력)

  <img width="571" alt="모고등급" src="https://user-images.githubusercontent.com/81000484/156864109-dfa0259e-06e6-463e-8b45-6d72b7e6ea05.png">

  st.write("2-2. 모고등급 ")

  c = st.text_area("각각 입력해주세요.", "국어:\n영어:\n수학:\n선택1:\n선택2:\n한국사:")

- selectbox(
