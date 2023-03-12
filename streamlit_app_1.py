#STREAMLIT APP 1 !!!!!!!!!!!!!!!!

import streamlit as st
st.text("ML APP1")

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])
st.write('You selected:', options)
