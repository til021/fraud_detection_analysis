import streamlit as st
import streamlit.components.v1 as components

# Sidebar


# Main Page

st.markdown("# Fraudes por Distância")

path_to_html = "graphs/fraudes_por_distância.html"

# Read file and keep in variable
with open(path_to_html, "r") as f:
    html_data = f.read()

## Show in webpage
st.components.v1.html(html_data, height=500)

st.markdown(
    "#### Como os dois gráficos possuem uma distribuição praticamente idêntica, não podemos afirmar que existe uma relação entre os casos de fraude e uma maior distância entre usuáriuo e comerciante."
)
