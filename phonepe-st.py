import pandas as pd
import mysql.connector
import streamlit as st
import plotly.express as px


# Establish the connection with mysql
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    database='phonepe_db1'
)
mycursor = connection.cursor(buffered=True)
mycursor.execute("use phonepe_db2")
def topcharts1() :

    # Year = st.slider("**Year**", min_value=2018, max_value=2022)
    # Quarter = st.slider("Quarter", min_value=1, max_value=4)
    #Year = st.selectbox('Select the year',(2018,2019,2020,2021,2022))
    #Quarter=st.selectbox('Select the quarter',(1,2,3,4))
    col1st,col2nd = st.columns(2)
    with col1st:
        Year = st.selectbox('Select the year', (2018, 2019, 2020, 2021, 2022))
    with col2nd:
        Quarter = st.selectbox('Select the quarter', (1, 2, 3, 4))

    #col1, col2, col3 = st.columns(3)#([1,2], gap="small")
    #with col1:

    st.markdown("### :violet[State]")
    mycursor.execute(
    f"select state, sum(trans_count) as Total_Transactions_Count, sum(trans_amt) as Total from agg_transaction where year = {Year} and quarter = {Quarter} group by state order by Total desc limit 10")
    df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Transactions_Count', 'Total_Amount'])
    #fig, ax = plt.subplots(figsize=(6, 6))
    fig = px.pie(df, values='Total_Amount',
                 names='State',
                 title='Top 10',
                 color_discrete_sequence=px.colors.sequential.Agsunset,
                 hover_data=['Transactions_Count'],
                 labels={'Transactions_Count': 'Transaction_Count'})

    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig.update_layout(title_font=dict(size=25))
    st.plotly_chart(fig, use_container_width=True)


    #with col2:

    st.markdown("### :violet[District]")
    mycursor.execute(
        f"select district , sum(count) as Total_Count, sum(amount) as Total from map_trans where year = {Year} and quarter = {Quarter} group by district order by Total desc limit 10")
    df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Transactions_Count', 'Total_Amount'])

    fig = px.pie(df, values='Total_Amount',
                 names='District',
                 title='Top 10',
                 color_discrete_sequence=px.colors.sequential.Agsunset,
                 hover_data=['Transactions_Count'],
                 labels={'Transactions_Count': 'Transactions_Count'})

    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)
    #with col3:
    st.markdown("### :violet[Pincode]")
    mycursor.execute(
        f"select pincode, sum(transaction_count), sum(transaction_amount) as Totalamount from top_transpin where year={Year} and quarter={Quarter} group by pincode order by Totalamount desc limit 10")
    df = pd.DataFrame(mycursor.fetchall(), columns=['Pincode', 'Transaction_count', 'Total_Trans_amount'])
    fig = px.pie(df, values='Total_Trans_amount',
                 names='Pincode',
                 title='Top 10',
                 color_discrete_sequence=px.colors.sequential.Agsunset,
                 hover_data=['Transaction_count'],
                 labels={'Transaction_count': 'Transaction_count'})
    fig.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)

def topcharts2():
    col1st, col2nd = st.columns(2)
    with col1st:
        Year = st.selectbox('Select the year', (2018, 2019, 2020, 2021, 2022))
    with col2nd:
        Quarter = st.selectbox('Select the quarter', (1, 2, 3, 4))
    #cols1, cols2, cols3= st.columns([2, 2, 2], gap="large")

    #with cols1:
    st.markdown("### :violet[Brand wise-Total users]")
    if Year == 2022 and Quarter in [2, 3, 4]:
        st.markdown("#### Sorry No Data to Display for 2022 Quarter 2,3,4")
    else:
        mycursor.execute(
            f"select brand,sum(count) as ccount, avg(percentage)*100 as Avg_Percentage from agg_user_dev where year={Year} and quarter={Quarter} group by brand order by ccount desc limit 10")
        df = pd.DataFrame(mycursor.fetchall(), columns=['Brand', 'Count', 'Percentage'])
        fig = px.pie(df, names='Brand', values='Count', title="Top 10",
                     color_discrete_sequence=px.colors.sequential.Agsunset,
                     hover_data=['Percentage'], labels={'Percentage': 'Percentage%'})
        st.plotly_chart(fig, use_container_width=True)

    #with cols2:
    st.markdown("### :violet[App opens]")
    mycursor.execute(
        f"select state,sum(app_open) as Total_app_opens,sum(Reg_users) as Total_RegUsers from map_user where year={Year} and quarter={Quarter} group by state order by Total_RegUsers desc limit 10")
    df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_app_opens', 'Total_RegUsers'])
    fig = px.pie(df, values='Total_RegUsers', names='State', title='Top 10',
                 hover_data=['Total_app_opens'], labels={'Total_app_opens': 'Total_app_opens'})
    st.plotly_chart(fig,use_container_width=True)

    #with cols3:
    st.markdown("### :violet[District wise total users]")
    mycursor.execute(
        f"select district, sum(Reg_Users) as Total_Users from top_user_state where year = {Year} and quarter = {Quarter} group by district order by Total_Users desc limit 10")
    df = pd.DataFrame(mycursor.fetchall(), columns=['District', 'Total_Users'])
    fig = px.pie(df,
                 values='Total_Users',
                 names='District',
                 title='Top 10',
                 color_discrete_sequence=px.colors.sequential.Agsunset,
                 hover_data=['Total_Users'])
    st.plotly_chart(fig,use_container_width=True)

def Explore_Data():
    Type = st.sidebar.selectbox("**Type**", ("Transactions", "Users"))
    col1, col2 = st.columns(2)
    with col1:
        Year = st.slider("**Year**", min_value=2018, max_value=2022)
    with col2:
        Quarter = st.slider("Quarter", min_value=1, max_value=4)
    if Type == "Transactions":
        st.markdown("## :violet[Overall State Data - Transactions Amount]")
        mycursor.execute(f"select state, sum(count) as Total_Transactions, sum(amount) as Total_amount from map_trans where year = {Year} and quarter = {Quarter} group by state order by state")
        df1 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Transactions', 'Total_amount'])
        fig = px.choropleth(df1,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Total_Transactions',
                            color_continuous_scale='sunset')

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("## :violet[Overall State Data - Transactions Count]")
        mycursor.execute(
            f"select state, sum(count) as Total_Transactions_count, sum(amount) as Total_amount from map_trans where year = {Year} and quarter = {Quarter} group by state order by state")
        df2 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Transactions_count', 'Total_amount'])
        fig=px.choropleth(df2,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                          featureidkey='properties.ST_NM',
                          locations='State',
                          color='Total_Transactions_count',
                          color_continuous_scale='sunset')
        fig.update_geos(fitbounds='locations',visible=False)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("## :violet[Top Payment Type]")
        mycursor.execute(
            f"select trans_type, sum(trans_count) as Total_Transactions_count, sum(trans_amt) as Total_Trans_amount from agg_transaction where year= {Year} and quarter = {Quarter} group by trans_type order by trans_type")
        df3 = pd.DataFrame(mycursor.fetchall(), columns=['Transaction_type', 'Total_Transactions_count', 'Total_amount'])
        fig=px.bar(df3,title='Transaction Types vs Total_Transactions',
                          x='Transaction_type',
                          y='Total_Transactions_count',
                   orientation='v',
                   color='Total_amount',
                   color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("# ")
        st.markdown("## :violet[Select any State to explore more]")
        selected_state = st.selectbox("",
                                      ('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'), index=30)

        mycursor.execute(
            f"select state, district,year,quarter, sum(count) as Total_Transactions_count, sum(amount) as Total_amount from map_trans where year = {Year} and quarter = {Quarter} and State = '{selected_state}' group by state, district,year,quarter order by state,district")

        df1 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'District', 'Year', 'Quarter',
                                                         'Total_Transactions', 'Total_amount'])
        fig = px.bar(df1,
                     title=selected_state,
                     x="District",
                     y="Total_Transactions",
                     orientation='v',
                     color='Total_amount',
                     color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig, use_container_width=True)

    if Type=="Users":
        st.markdown("## :violet[Overall State Data - User App opening frequency]")
        mycursor.execute(
            f"select state, sum(Reg_users) as Total_Users, sum(app_open) as Total_App_opens from map_user where year = {Year} and quarter = {Quarter} group by state order by state")
        df3 = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Total_Users', 'Total_App_opens'])
        fig = px.choropleth(df3,
                            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                            featureidkey='properties.ST_NM',
                            locations='State',
                            color='Total_App_opens',
                            color_continuous_scale='sunset')

        fig.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("## :violet[Select any State to explore more]")
        selected_state = st.selectbox("",
                                     ('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar',
                                       'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu',
                                       'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                       'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh',
                                       'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
                                       'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana',
                                       'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'), index=30)
    mycursor.execute(f"select state,year,quarter,district,sum(Reg_users) as Total_Users, sum(app_open) as Total_App_opens from map_user where year = {Year} and quarter = {Quarter} and state = '{selected_state}' group by state, district,year,quarter order by state,district")
    df4=pd.DataFrame(mycursor.fetchall(), columns=['State','Year','Quarter','District','Total_users','Total App opens'])
    fig = px.bar(df4,
                 title=selected_state,
                 x="District",
                 y="Total_users",
                 orientation='v',
                 color='Total_users',
                 color_continuous_scale=px.colors.sequential.Agsunset)
    st.plotly_chart(fig, use_container_width=True)
def Home():
    st.title(":violet[Phonepe Pulse Data Visualization and Exploration]")
    st.markdown("### :violet[A User-Friendly Tool Using Streamlit and Plotly]")
def About():
    st.markdown("### :violet[This is a user-friendly and easily accessible dashboard that provide valuable insights and information about the data in the Phonepe pulse Github repository.]")

def set_page_config():
    st.set_page_config(
          page_title="Phonepe Pulse",
              )

    selected = st.sidebar.selectbox("Menu", ["Home", "Top_Charts", "Explore_Data", "About"],

                            index=0,
                            key="menu",
                            help="Select an option from the menu")
    if selected=="Top_Charts":
        Type=st.sidebar.selectbox('Type',('Transactions','Users'))
        if Type=='Transactions':
            topcharts1()
        if Type=='Users':
            topcharts2()
    if selected=="Explore_Data":
        Explore_Data()
    if selected=='Home':
        Home()
    if selected=="About":
        About()

    #tab1, tab2 = st.tabs(["Top_charts", "Explore _Data"])
    # with tab1:
    #     topcharts()
#st.selectbox("Menu", ["Home", "Top_Charts", "Explore_Data", "About"])


if __name__ == '__main__':
   set_page_config()


