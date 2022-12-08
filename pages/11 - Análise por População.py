import streamlit as st
import streamlit.components.v1 as components

# Sidebar

graph = add_selectbox = st.sidebar.selectbox(
    "Como você quer visualizar o gráfico?", ("Box Plot", "ECDF Plot")
)


# Main Page

st.markdown("# Fraudes por População")
st.write("Escolha uma das opções ao lado para alterar o tipo de gráfico.")


if graph == "Box Plot":
    path_to_html = "graphs/fraudes_por_população_box.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)

elif graph == "ECDF Plot":
    path_to_html = "graphs/fraudes_por_city_pop_ecdf.html"

    # Read file and keep in variable
    with open(path_to_html, "r") as f:
        html_data = f.read()

    ## Show in webpage
    st.components.v1.html(html_data, height=500)

st.markdown(
    """#### Não há indicios de relação entre a quantidade de fraudes e o aumento da população.
"""
)
