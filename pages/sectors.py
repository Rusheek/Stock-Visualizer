import streamlit as st
from utils import global_data as gd

st.write('Inside sectors page')
option_sector = st.selectbox("Select the sector from dropdown",['Auto','Tech'],index=None)
st.write("You have selected:", option_sector    )