import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/IMG_20160604_postema.jpg")

with col2:
    st.title("Hans Postema")
    content = """
    Hallo, ik ben Hans! Ik ben huisarts met een grote interesse voor programmeren.
    Inmiddels heb ik een aantal programmas geschreven in verschillende talen.
    Waaronder Java (android), Javascript, php (Joomla!), Visual Basic (Excel) en nu Python.
    """
    st.info(content)
