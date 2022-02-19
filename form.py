import streamlit as st

st.header("독서와 성적의 상관관계")
st.subheader("----------------------------------------------------------------------")

#st.write("1. ")
#checkbox_btn = st.checkbox("..")
# if checkbox_btn:
#     st.write("Thank You!")

#checkbox_btn2 = st.checkbox("..", value = True)
# if checkbox_btn2:
#     st.write("Thank You!")

#1
st.write("1. 성별 ")
a = st.radio ("성별을 골라주세요.", ("남", "여"))

#2
st.write("2-1. 내신등급 ")
b = st.text_input("소수점 첫째 자리까지 입력해주세요.")

#3
st.write("2-2. 모고등급 ")
c = st.text_area("각각 입력해주세요.", "국어:\n영어:\n수학:\n선택1:\n선택2:\n한국사:")

#4
st.write("3. 학교")
d = st.selectbox("자신이 속한 고등학교 계열을 골라주세요.", ("일반계고등학교", "외고/국제고/과학고/영재고", "특성화고등학교", "자율형고등학교", "예술고/체육고"))

#5
st.write("4. 독서를 매일 꾸준히 한 기간")
e = st.slider('나이로 답해주세요.', 0.0, 20.0, (5.0, 15.0))
st.write('Values:', e)

#6
st.write("5. 위 기간에서의 한 달 평균 독서량  ")
#st.time_input("Time")
f = st.number_input("권 수를 입력해주세요.",(1))

#7
st.write("6. 현재 한 달 평균 독서량  ")
#st.time_input("Time")
g = st.number_input("권 수를 입력해주세요.",(0))

# 저장
num = 0
sa = open("성별.txt", 'w')
sb = open("내신등급.txt", 'w')
sc = open("모고등급.txt", 'w')
sd = open("학교.txt", 'w')
se = open("독서기간.txt", 'w')
sf = open("독서량1.txt", 'w')
sg = open("독서량2.txt", 'w')

if st.button("완료"):
    num += 1
    st.write("저장 완료. 감사합니다!")
    sa.write(a)
    sa.close()
    sb.write(b)
    sb.close()
    sc.write(c)
    sc.close()
    sd.write(d)
    sd.close()
    #se.write(e)
    #se.close()
    # sf.write(f)
    # sf.close()
    # sg.write(g)
    # sg.close()

