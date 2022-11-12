import streamlit as st

header = st.beta_container()
temp_conv = st.beta_container()
tiro = st.beta_container()


def cel2far(c):
    return c*9/5+32


with header:
    st.title('Informática y Programación')
    st.header('Grado en Ingeniería Física')
    st.text('Universitat Politècnica de Valéncia')
    
with temp_conv:
    st.title('Conversor grados')
    tc = st.slider('Temperatura Celsius', min_value=-50, max_value=50, value=0)

    if st.button('Convertir'):
        tf = cel2far(tc)
        st.text_input('Fahrenheit: ', value=tf)
