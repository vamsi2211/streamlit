#STREAMLIT APP 1 !!!!!!!!!!!!!!!!

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="*BHANU.............................",page_icon="🧑‍💻", layout="centered")
st.text("ML APP1")
train = pd.DataFrame({'col1':list(range(10)),'col2':list(range(10)),'col3':list(range(10))})
a = train.columns
num_opt = st.multiselect('What are your numerical columns',a)
cat_opt = st.multiselect('What are your categorical columns',[x for x in a if x not in num_opt])
date_opt = st.multiselect('What are your datetime columns',[x for x in a if x not in num_opt+cat_opt])
st.write('Numerical columns:',num_opt,'Categorical columns:',cat_opt,'date columns:',date_opt)
with st.form(key='columns_in_form'):
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        initialInvestment = st.text_input("Starting capital",value=500)
    with c2:
        monthlyContribution = st.text_input("Monthly contribution (Optional)",value=100)
    with c3:
        annualRate = st.text_input("Annual increase rate in percentage",value="15")
    with c4:
        investingTimeYears = st.text_input("Duration in years:",value=10)

    submitButton = st.form_submit_button(label = 'Calculate')


