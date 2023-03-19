#STREAMLIT APP 1 !!!!!!!!!!!!!!!!

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="MLAPP",page_icon="🧑‍💻", layout="centered")
st.text("ML APP1")
train = pd.DataFrame({'col1':list(range(10)),'col2':list(range(10)),'col3':list(range(10))})
a = train.columns
num_opt = st.multiselect('What are your numerical columns',a)
cat_opt = st.multiselect('What are your categorical columns',[x for x in a if x not in num_opt])
date_opt = st.multiselect('What are your datetime columns',[x for x in a if x not in num_opt+cat_opt])
st.write('Numerical columns:',num_opt,'Categorical columns:',cat_opt,'date columns:',date_opt)

    initialInvestment = st.text_input("Starting capital",value=500)
    monthlyContribution = st.text_input("Monthly contribution (Optional)",value=100)
    annualRate = st.text_input("Annual increase rate in percentage",value="15")
    investingTimeYears = st.text_input("Duration in years:",value=10)
    sel1= form.selectbox("Report Type", ("normal", "full"))
    track= form.text_input("enter track no").upper()

if submit:
    st.success('The output is this x')
