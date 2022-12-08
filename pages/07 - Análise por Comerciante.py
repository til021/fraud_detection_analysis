import streamlit as st
import streamlit.components.v1 as components

# Sidebar

graph = add_selectbox = st.sidebar.selectbox(
    "Fraudes Praticadas por Comerciante: ", ("Scatter Plot", "KDE Plot"), key=1
)

seccond_graph = add_selectbox = st.sidebar.selectbox(
    "Frequência de Fraudes Praticadas (em Dias): ",
    ("Box Plot", "Violin Plot"),
    key=2,
)

third_graph = add_selectbox = st.sidebar.selectbox(
    "Frequência de Fraudes Praticadas (em 100 Dias): ",
    ("Box Plot", "Violin Plot"),
    key=3,
)

# Main Page

st.markdown("# Fraudes por Comerciante")
st.write("Escolha uma das opções ao lado para alterar o tipo de gráfico.")


if graph == "Scatter Plot":
    path_to_html = "graphs/fraudes_por_comerciante_scatter.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)

elif graph == "KDE Plot":
    path_to_html = "graphs/fraudes_por_comerciante_kde.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)

st.markdown(
    """#### A maioria dos comerciantes que cometem fraudes realizam o esquema até 10 vezes - no período analisado. 
#### É necessário analizar o lapso de tempo entre uma fraude e outra para obter maiores conclusões. """
)

if seccond_graph == "Violin Plot":
    path_to_html = "graphs/violin_repetição_frauds_comerciante_dias.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)

elif seccond_graph == "Box Plot":
    path_to_html = "graphs/box_repetição_frauds_comerciante_dias.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)

st.markdown(
    """#### A maioria dos comerciantes que cometem fraudes tendem a repetir a fraude em um curto espaço de tempo - menos de 20 dias!
#### Considerando a frequência de fraudes nas vítimas, os comerciantes que cometem mais fraudes executam elas em poucas horas!"""
)

if third_graph == "Violin Plot":
    path_to_html = "graphs/violin_repetição_frauds_comerciante_100dias.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)

elif third_graph == "Box Plot":
    path_to_html = "graphs/box_repetição_frauds_comerciante_100dias.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)
