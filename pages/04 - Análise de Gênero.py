import streamlit as st
import streamlit.components.v1 as components

# Sidebar:
# We don't have a side bar

# Main Page:

st.markdown("# Fraudes por Gênero")


path_to_html = "graphs/fraudes_por_genero.html"

# Read file and keep in variable
with open(path_to_html, "r") as f:
    html_data = f.read()

## Show in webpage
st.components.v1.html(html_data, height=500)

st.markdown(
    """#### Apesar de termos menos homens que mulheres em nossa base de dados, é possível observar que a quantidade de fraudes envolvendo os dois gêneros é praticamente a mesma.

#### Assim, existe uma maior tendência a tentativas de fraude se o indivíduo for do sexo masculino."""
)
