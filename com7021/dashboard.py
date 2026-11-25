"""
    Streamlit dashboard for Eco-Move
"""

import streamlit as st
import pandas as pd

df = pd.read_excel('[5442] EcoMoveMobility.xlsx')
st.write('Eco-Move Mobility Dashboard')
st.write(df)
st.dataframe(df.head())