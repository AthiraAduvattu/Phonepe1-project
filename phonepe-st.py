import streamlit as st
import numpy as np
import requests
import json
import os
import mysql.connector

# Establish the connection
connection = mysql.connector.connect(
                                        host = 'localhost',
                                        user = 'root',
                                        password = 'root123',
                                        database='phonepe_db1'
                                    )
mycursor=connection.cursor(buffered=True)
mycursor.execute("use phonepe_db1")
def topcharts():
    Year = st.slider("**Year**", min_value=2018, max_value=2022)
    Quarter = st.slider("Quarter", min_value=1, max_value=4)
    mycursor.execute(
        f"select state, sum(trans_count) as Total_Transactions_Count, sum(trans_amt) as Total from agg_transaction where year = {Year} and quarter = {Quarter} group by state order by Total desc limit 10")
    df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Transactions_Count', 'Total_Amount'])
    fig = px.pie(df, values='Total_Amount',
                 names='State',
                 title='Top 10',
                 color_discrete_sequence=px.colors.sequential.Agsunset,
                 hover_data=['Transactions_Count'],
                 labels={'Transactions_Count': 'Transaction_Count'})

    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)
def set_page_config():
    st.set_page_config(
          page_title="Phonepe Pulse",
              )
    st.title(":violet[Phonepe Pulse Data Visualization and Exploration]")
    selected = st.sidebar.selectbox("Menu", ["Home", "Top_Charts", "Explore_Data", "About"],

                            index=0,
                            key="menu",
                            help="Select an option from the menu")
    Type=st.sidebar.selectbox('Type',('Transactions','Users'))
    if Type=='Transactions':
        topcharts()
    #tab1, tab2 = st.tabs(["Top_charts", "Explore _Data"])
    # with tab1:
    #     topcharts()
#st.selectbox("Menu", ["Home", "Top_Charts", "Explore_Data", "About"])


if __name__ == '__main__':
    set_page_config()