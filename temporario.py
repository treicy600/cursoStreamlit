import streamlit as st
import pandas as pd
st.header("Cabeçalho")

st.multiselect(
  'Quais são suas cores favoritas?',
  ['verde', 'amarelo', 'vermelho', 'azul'],
  ['amarelo', 'vermelho'])
st.color_picker("Pick A Color", "#00f900")
st.feedback("stars")

df = pd.DataFrame(
  [
    {"command": "st.selectbox", "rating": 4, "is_widget": True},
    {"command": "st.balloons", "rating": 5, "is_widget": False},
    {"command": "st.time_input", "rating": 3,"is_widget": True},
  ]
)
edited_df = st.data_editor(df)
st.toggle("toggle")
st.text_area("Enter text")
st.text_input("")
st.button("Botão salvar")
st.selectbox(
  'Qual a sua cor favorita?',
  ('Azul', 'Vermelho', 'verde'))

st.checkbox('Sorvete')
st.checkbox('café')
st.checkbox('Refrigerante')

options = ["North", "East", "south", "west"]
selection = st.pills("Directions", options, selection_mode="multi")
st.button("Botão Salvar")
