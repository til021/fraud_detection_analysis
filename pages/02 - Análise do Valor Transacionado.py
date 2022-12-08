import streamlit as st
import streamlit.components.v1 as components

# Sidebar

graph = add_selectbox = st.sidebar.selectbox(
    "Como você quer visualizar o gráfico?", ("Box Plot", "ECDF Plot")
)

# Main Page
st.markdown("# Fraudes por Valor Transacionado")
st.write("Escolha uma das opções ao lado para alterar o tipo de gráfico.")

if graph == "Box Plot":
    path_to_html = "graphs/fraudes_por_valor_box.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=400)

elif graph == "ECDF Plot":
    path_to_html = "graphs/fraudes_por_valor_ecdf.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=400)

st.markdown(
    """#### Através do Boxplot podemos identificar uma clara distinção entre operações normais e operações fraudulentas avaliando o valor transacionado.  
    
#### Já na curva ECDF, operações não fraudulentas são bem distribuídas quando abaixo dos 1000 dólares.  

#### Por outro lado, existem dois intervalos de operação para as operações fraudulentas: abaixo de 25 dólares, e entre 250 e mil dólares."""
)
