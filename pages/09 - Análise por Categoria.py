import streamlit as st
import streamlit.components.v1 as components

# Sidebar


# Main Page

st.markdown("# Fraudes por Categoria")

path_to_html = "graphs/fraudes_por_categoria_oc.html"

# Read file and keep in variable
with open(path_to_html, "r") as f:
    html_data = f.read()

## Show in webpage
st.components.v1.html(html_data, height=500)

path_to_html = "graphs/fraudes_por_categoria_percent.html"

# Read file and keep in variable
with open(path_to_html, "r") as f:
    html_data = f.read()

## Show in webpage
st.components.v1.html(html_data, height=500)

st.markdown(
    "#### Não escobri o significado de cada categoria, mas está ai a distribuição de fraudes."
)
