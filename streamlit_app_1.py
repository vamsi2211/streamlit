#STREAMLIT APP 1 !!!!!!!!!!!!!!!!

import streamlit as st
st.text("ML APP1")
a = ['col1','col2','col3','col4','col5'
options = st.multiselect(
    'What are your favorite colors',
    a)
