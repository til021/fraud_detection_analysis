import streamlit as st
import streamlit.components.v1 as components

# Sidebar

graph = add_selectbox = st.sidebar.selectbox(
    "Como você quer visualizar o gráfico?", ("Box Plot", "ECDF Plot")
)


# Main Page

st.markdown("# Fraudes por Idade")
st.write("Escolha uma das opções ao lado para alterar o tipo de gráfico.")

if graph == "Box Plot":
    path_to_html = "graphs/fraudes_por_idade_box.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=400)

elif graph == "ECDF Plot":
    path_to_html = "graphs/fraudes_por_idade_ecdf.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=400)

elif graph == "KDE Plot":
    path_to_html = "graphs/fraudes_por_idade_kde.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=400)

st.markdown(
    """#### Avaliando os gráficos, podemos considerar uma tendência de sujeição à fraude levemente maior em pessoas mais velhas.  
    
#### Tal discrepância é observada com com mais facilidade em pessoas acima dos 40 anos."""
)
