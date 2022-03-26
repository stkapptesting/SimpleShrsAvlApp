import pandas as pd 
import streamlit as st 
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from ftplib import FTP
from io import BytesIO


#Static Way, download the file manually and put into the codebas itself which does not need any of the code from FTP to flo...
 
ftp = FTP("ftp3.interactivebrokers.com")
ftp.login(user="shortstock")

# Store file locally on run time
with open ("usa.txt", 'wb') as fp:
    ftp.retrbinary('RETR usa.txt', fp.write)


#Do not store the file but load directly into data frame
#flo = BytesIO()
#ftp.retrbinary('RETR usa.txt', flo.write)
#flo.seek(0)

st.set_page_config(page_title="IB File", layout="wide") 
st.title("Shares Avail Stats")

#shows = pd.read_csv("./usa.txt",on_bad_lines='warn',sep="|")  
#shows = pd.read_csv(flo,  on_bad_lines='warn', sep="|", header=1, skiprows = 0, usecols=range(8))

shows = pd.read_csv("usa.txt", sep="|", header=1, skiprows = 0, usecols=range(8))
gb = GridOptionsBuilder.from_dataframe(shows)

# add this
gb.configure_pagination()
gb.configure_side_bar()
gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
gridOptions = gb.build()

AgGrid(shows, gridOptions=gridOptions, enable_enterprise_modules=True)