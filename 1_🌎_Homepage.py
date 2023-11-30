import streamlit as st
from PIL import Image

st.set_page_config(page_title= "WebPage", layout= "wide")

with st.container():
    st.markdown("<h1 style= 'text-align: right_side'>Homepage</h1>", unsafe_allow_html= True)
    st.markdown("------") 

with st.container():
    st.header("Hi :wave: , I'm John")
    st.subheader("How I started learning progrmming")
    st.write(
        """
    I started learning programming when I discovered mods in "Minecraft: Java Edition",
    I wanted to make my own mod/s, I started learning java and java.script for the sole purpose on making my
    own private mod/s, another reason is there are few mods available in fabric, fabric is my favorite modloader
    because it loads the mods faster than forge(this is my own opinion and perspective, pls don't be offended).
"""
    )

with st.container():
    st.sidebar.success("Select a page above.")