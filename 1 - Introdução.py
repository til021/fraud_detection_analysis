import streamlit as st

# streamlit run "1 - Introdução.py"

st.title("Fraudes em Cartões de Crédito")

st.subheader(
    "Esta é uma análise gráfica, feita em um banco de dados simulado, \
    que contém transações legítimas e fraudulentas de usuários de cartão de crédito."
)

st.write(
    "O banco de dados foi criado através do Sparkov \
    e contém transações em cartões de 1000 clientes, \
    em operações realizadas com uma amostra de 800 comerciantes. \
    O período considerado foi de Janeiro de 2019 a Dezembro de 2020."
)

st.write(
    "Mais informações em: \
    <https://www.kaggle.com/datasets/kartik2112/fraud-detection?select=fraudTest.csv>"
)
st.caption("by Tiago C O Lima")
