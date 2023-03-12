#STREAMLIT APP 1 !!!!!!!!!!!!!!!!

import streamlit as st
st.text("ML APP1")

a = ['col1','col2','col3','col4','col5']
num_opt = st.multiselect('What are your numerical columns',a)
cat_opt = st.multiselect('What are your categorical columns',a)
date_opt = st.multiselect('What are your datetime columns',a)
st.write('Numerical columns:',num_opt)
st.write('Categorical columns:',cat_opt)
st.write('date columns:',date_opt)



