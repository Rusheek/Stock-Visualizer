import streamlit as st
from utils import global_data as gd

st.write('Inside sectors page')
# st.write(gd.sectors)
option_sector = st.selectbox("Select the sector from dropdown",gd.sectors,index=None)
st.write("You have selected:", option_sector)

if option_sector is not None:

    stocks_list = gd.nifty_df[gd.nifty_df['Sector'] == option_sector]['Ticker'].tolist()

    stock =  st.selectbox('Select the item you want:', stocks_list,index=None,)

    if stock is not None:
        #TODO add the code for displaying charts (Integration)
        # fetch the data of selected stock and display charts 
        # try async call for calling the functions

        
    
        selected_options = st.multiselect('Pick the stocks you would like to compare',stocks_list)

        if len(selected_options)>1:
            st.write(selected_options)
        else:
            st.write('You have selected :',selected_options)
            st.warning('Please pick more than one stock')

