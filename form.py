import streamlit as st

st.write("1. ")
checkbox_btn = st.checkbox("남")
if checkbox_btn:
    st.write("Thank You!")

checkbox_btn2 = st.checkbox("여", value = True)
if checkbox_btn:
    st.write("Thank You!")

selected_item = st.radio("a", "b", "c")