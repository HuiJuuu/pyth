import streamlit as st
import pandas as pd
import numpy as np

col1, col2, col3 = st.beta_columns(3)

with col1:
    st.header("A cat")
    #st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width = True)
    st.image("https://www.queen.co.kr/news/photo/201910/320536_59033_3350.jpg", use_column_width=True)

with col2:
    st.header("Button")
    if st.button("Button!!"):
        st.write("Yes")

with col3:
    st.header("Chart Data")
    chart_data = pd.DataFrame(np.random.randn(50,4), columns = ["a", "b", "c", "d"])
    st.bar_chart(chart_data)
