import streamlit as st

st.header("Cabeçalho")

st.multiselect(
  'Quais são suas cores favoritas?',
  ['verde', 'amarelo', 'vermelho', 'azul'],
  ['amarelo', 'vermelho'])

st.toggle("toggle")
st.text_area("Enter text")
st.text_input("")
st.button("Botão salvar")
st.selectbox(
  'Qual a sua cor favorita?',
  ('Azul', 'Vermelho', 'verde'))
st.button("Botão Salvar")
