#STREAMLIT APP 1 !!!!!!!!!!!!!!!!

import pandas as pd
import numpy as np
import streamlit as st

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)