#STREAMLIT APP 1 !!!!!!!!!!!!!!!!

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="MLAPP",page_icon="🧑‍💻", layout="centered")
st.text("ML APP1")
train = pd.DataFrame({'col1':list(range(10)),'col2':list(range(10)),'col3':list(range(10)),'col6':[chr(x) for x in range(65,75)], 'col5':[chr(x) for x in range(97,97+10)]})
a = train.columns
num_opt = st.multiselect('What are your numerical columns',a)
cat_opt = st.multiselect('What are your categorical columns',[x for x in a if x not in num_opt])
date_opt = st.multiselect('What are your datetime columns',[x for x in a if x not in num_opt+cat_opt])
st.write('Numerical columns:',num_opt,'Categorical columns:',cat_opt,'date columns:',date_opt)
if submit:
    st.success('The output is this x')
