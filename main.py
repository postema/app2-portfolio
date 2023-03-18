import streamlit as st
import pandas

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

content2 = """
Hieronder vind u een aantal apps die ik geschreven heb in Python. 
U mag natuurlijk ook contact met mij opnemen.
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"{row['language']} : [Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"{row['language']} : [Source Code]({row['url']})")
