import streamlit as st
import streamlit.components.v1 as components

# Sidebar

# Main Page

st.markdown("# Fraudes por Período")

path_to_html = "graphs/fraudes_por_hora_dia.html"

# Read file and keep in variable
with open(path_to_html, "r") as f:
    html_data = f.read()

## Show in webpage
st.components.v1.html(html_data, height=500)

st.markdown(
    """#### Esse gráfico é muito interessante! As operações não fraudulentas ocorrem de forma praticamente constante ao longo do dia.
#### Porém, as operações fraudulentas tendem a se concentrar entre as 22h da noite e as 3h da madrugada!"""
)

path_to_html = "graphs/fraudes_por_dia_semana.html"

# Read file and keep in variable
with open(path_to_html, "r") as f:
    html_data = f.read()

## Show in webpage
st.components.v1.html(html_data, height=500)

st.markdown(
    """#### Não é possível indicar um dia da semana que seja mais sujeito a fraudes. A ocorrência de fraudes acompanha a variação das operações ao longo dos dias. 
#### É possível inferir que as pessoas gastam menos durante a semana que no final de semana."""
)

path_to_html = "graphs/fraudes_por_mês.html"

# Read file and keep in variable
with open(path_to_html, "r") as f:
    html_data = f.read()

## Show in webpage
st.components.v1.html(html_data, height=500)

st.markdown(
    """#### Majoritariamente, ao longo do ano, as fraudes acompanham o nível de gastos da população.
#### Porém, existe um aumento expressivo de fraudes em janeiro e fevereiro, quando comparado aos níveis de transações normais.
#### Ou seja, existe um aumento de fraudes após as compras natalinas e festividades de ano novo. Por outro lado, as fraudes diminuem na época do natal.
#### Possivelmente os comerciantes evitam cometer fraudes assim que conseguem as informações dos clientes, esperando alguns meses para cometer o delito."""
)
