import pandas as pd 
import streamlit as st 
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from ftplib import FTP



st.set_page_config(page_title="IB File", layout="wide") 
st.title("Shares Avail Stats")

shows = pd.read_csv("./usa.txt",on_bad_lines='warn',sep="|")  
gb = GridOptionsBuilder.from_dataframe(shows)

# add this
gb.configure_pagination()
gb.configure_side_bar()
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
gridOptions = gb.build()

AgGrid(shows, gridOptions=gridOptions, enable_enterprise_modules=True)