import streamlit as st
import streamlit.components.v1 as components

# Sidebar

graph = add_selectbox = st.sidebar.selectbox(
    "Fraudes Sofridas por Consumidor: ", ("Scatter Plot", "KDE Plot"), key=1
)

seccond_graph = add_selectbox = st.sidebar.selectbox(
    "Frequência de Fraudes Sofridas (em Dias): ",
    ("Box Plot", "Violin Plot"),
    key=2,
)

third_graph = add_selectbox = st.sidebar.selectbox(
    "Frequência de Fraudes Sofridas (em Horas): ",
    ("Box Plot", "Violin Plot"),
    key=3,
)

# Main Page

st.markdown("# Fraudes por Consumidor")
st.write("Escolha uma das opções ao lado para alterar o tipo de gráfico.")


if graph == "Scatter Plot":
    path_to_html = "graphs/fraudes_por_pessoa_scatter.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)

elif graph == "KDE Plot":
    path_to_html = "graphs/fraudes_por_pessoa_kde.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)

st.markdown(
    """#### Analisando os gráficos, percebemos que, se a pessoa está propensa a ser fraudada, essa pessoa sofrerá em média 10 operações fraudulentas.
#### A distribuição das fraudes sofridas segue a curva normal."""
)

if seccond_graph == "Violin Plot":
    path_to_html = "graphs/violin_repetição_frauds_dias.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)

elif seccond_graph == "Box Plot":
    path_to_html = "graphs/box_repetição_frauds_dias.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)

    st.markdown(
        """#### O tempo de repetição da fraude na vítima é muito curto! A vítima pode ser fraudada diversas vezes na mesma hora!
#### Algumas vezes os fraudadores esperam até de noite para realizar a fraude!"""
    )

if third_graph == "Violin Plot":
    path_to_html = "graphs/violin_repetição_frauds_horas.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)

elif third_graph == "Box Plot":
    path_to_html = "graphs/box_repetição_frauds_horas.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)
