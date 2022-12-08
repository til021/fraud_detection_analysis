import streamlit as st
import streamlit.components.v1 as components

# Sidebar


# Main Page

st.markdown("# Fraudes por Volume de Transações")


path_to_html = "graphs/transações_por_comerciante_scatter.html"

# Read file and keep in variable
with open(path_to_html, "r") as f:
    html_data = f.read()

## Show in webpage
st.components.v1.html(html_data, height=500)


st.markdown(
    """#### O gráfico representa a quantidade de fraudes cometidas por comerciantes em relação ao seu volume total de transações.
#### Aparentemente existem clústers na relação entre as fraudes e o volume de vendas. Não obtive nenhuma ideia do que pode causar isso.
"""
)
