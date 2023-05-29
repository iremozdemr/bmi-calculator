import streamlit as st

st.title(":blue[bmi calculator]")
#blue green red violet orange

gender = st.radio("gender:",("male","female"))
age = st.slider("age",18,65)

height = st.number_input("height(m)",1.30)
weight = st.number_input("weight(kg)",35)

body_mass_index = weight/(height*height)
if body_mass_index<= 18.5:
    result = "underweight"
elif 18.5 < body_mass_index <= 24.9:
    result = "normal weight"
elif 24.9 < body_mass_index <= 29.9:
    result = "overweight"
elif 29.9 < body_mass_index:
    result = "obesity"

if st.button("calculate"):
    st.success(result)
