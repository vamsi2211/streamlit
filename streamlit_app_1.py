#STREAMLIT APP 1 !!!!!!!!!!!!!!!!

import streamlit as st

st.set_page_config(page_title="*BHANU.............................",page_icon="🧑‍💻", layout="centered")
st.text("ML APP1")

a = train.columns
num_opt = st.multiselect('What are your numerical columns',a)
cat_opt = st.multiselect('What are your categorical columns',[x for x in a if x not in num_opt])
date_opt = st.multiselect('What are your datetime columns',[x for x in a if x not in cat_opt])
st.write('Numerical columns:',num_opt,'Categorical columns:',cat_opt,'date columns:',date_opt)


