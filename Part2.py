import streamlit as st

st.header("Subheader")
st.write("abc")
if st.button("Click Button"):
    st.write("Hello test")

#2. Check Box
checkbox_btn = st.checkbox("Checkbox button")
if checkbox_btn:
    st.write("Good!")

# If you want to default value = True
checkbox_btn2 = st.checkbox("Checkbox button2", value = True)

if checkbox_btn2:
    st.write("Good!")

#Radio button
selected_item = st.radio("Radio Button", ("hi", "hello", "bye"))

if selected_item == "hi":
    st.write("HIIIIII")
elif selected_item == "hello":
    st.write("HELOOOOOO")
elif selected_item == "bye":
    st.write("BYEEEEE")

#select box
option = st.selectbox("Please select in selctbox!", ("hm", "hi", "kk"))
st.write("option is", option)
#Multiple box
multi_option = st.multiselect("Please select multi box", ("a", "b", "c"))
st.write("you selected", multi_option)

#slider
values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)