import streamlit as st
from PIL import Image

st.set_page_config(page_title= "WebPage", layout= "wide")

IMG= Image.open("images/Untitled.png")

with st.container():
    st.markdown("<h1 style= 'text-align: right_side'>Projects</h1>", unsafe_allow_html= True)
    st.markdown("------")

with st.container():
    col1, col2= st.columns((1, 2))
    with col1:
        st.write("""
    This is my first project using streamlit, it's a web photo editor I programmed because I was too lazy to install a photo editor.
""")
        st.write("Photo Editor -https://tsltuv-tppe-photoeditor-gyyeks.streamlit.app/")

    with col2:
        st.image(IMG)

with st.container():
    st.sidebar.success("Select a page above.")