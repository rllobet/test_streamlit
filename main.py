import streamlit as st

def cel2far(c):
    return c*9/5+32


st.title('Conversor grados')
tc = st.slider('Temperatura Celsius', min_value=-50, max_value=50, value=0)

if st.button('Convertir'):
    tf = cel2far(tc)
    st.text_input('Fahrenheit: ', value=tf)
