import streamlit as st
import logic
import logic.load_data
from utils import global_data as gd
import datetime
import asyncio

async def main():
    await logic.load_data.set_global_data()
    
asyncio.run(main())

gd.start_date = st.date_input('Enter Start Date',min_value=datetime.date(2020,1,1),value=datetime.date(2020,1,1))
gd.end_date = st.date_input('Enter End Date',max_value='today',value='today')

st.write('start date is :',gd.start_date)
st.write('end date is :', gd.end_date)



