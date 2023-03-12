#STREAMLIT APP 1 !!!!!!!!!!!!!!!!

import streamlit as st

st.set_page_config(page_title="ML APP 1                    .",page_icon="🧑‍💻", layout="centered")
st.text("ML APP1")

a = ['col1','col2','col3','col4','col5']
num_opt = st.multiselect('What are your numerical columns',a)
cat_opt = st.multiselect('What are your categorical columns',a)
date_opt = st.multiselect('What are your datetime columns',a)
st.write('Numerical columns:',num_opt,'Categorical columns:',cat_opt,'date columns:',date_opt)



