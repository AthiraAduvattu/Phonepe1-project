#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os
import json
import pprint
import pandas as pd
import git
import mysql.connector
import plotly.express as px

# In[5]:


response = requests.get('https://api.github.com/repos/PhonePe/pulse')
repo = response.json()
clone_url = repo['clone_url']

repo_name = "pulse"
clone_dir = os.path.join(os.getcwd(), repo_name)

# In[2]:


import pprint

pprint.pprint(response)

# In[8]:


pprint.pprint(repo)

# In[10]:


pip
install
gitpython

# In[2]:


import git

# In[3]:


repository_url = "https://github.com/phonepe/pulse.git"
local_directory = "phonepe_pulse"
git.Repo.clone_from(repository_url, local_directory)

# In[3]:


os.listdir("C:\\Users\\HP\\phonepe_pulse\\.git")

# In[4]:


import pandas as pd

path = "C:/Users/HP/phonepe_pulse/data/aggregated/transaction/country/india/state"
Agg_state = os.listdir(path)

Agg_state


# In[54]:


# def format_amount(scientific_value):
#     return '{:,.2f}'.format(scientific_value)


# In[5]:


def scientific_to_amount(scientific_notation):
    # Convert scientific notation to a float
    number = float(scientific_notation)

    # Format the float as a string with two decimal places
    formatted_amount = '{:.2f}'.format(number)

    return formatted_amount


# In[96]:


scientific_to_float(1.845307e+06)

# In[110]:


D1 = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [], 'Transaction_amount': []}
for i in Agg_state:
    p = path + "/" + i
    Agg_yr = os.listdir(p)
    for y in Agg_yr:
        M = p + "/" + y
        Agg_yr_list = os.listdir(M)

        for k in Agg_yr_list:
            N = M + "/" + k
            Data = open(N, 'r')
            A = json.load(Data)
            for v in A['data']['transactionData']:
                Name = v["name"]
                count = v["paymentInstruments"][0]['count']
                amount = scientific_to_amount(v["paymentInstruments"][0]['amount'])
                D1["Transaction_type"].append(Name)
                D1["Transaction_count"].append(count)
                D1["Transaction_amount"].append(amount)
                D1["State"].append(i)
                D1["Year"].append(y)
                D1["Quarter"].append(int(k.strip('.json')))
df1 = pd.DataFrame(D1)
df1.to_csv('Agg_trans1.csv')

# In[57]:


format_amount(1.213866e+07)

# In[111]:


df1

# In[59]:


# In[119]:


path = "C:/Users/HP/phonepe_pulse/data/aggregated/user/country/india/state"
D2 = {'State': [], 'Year': [], 'Quarter': [], 'Brand': [], 'count': [], 'Percentage': []}
Agg_state = os.listdir(path)
for i in Agg_state:
    p = path + "/" + i
    agg_yr = os.listdir(p)
    for y in agg_yr:
        p2 = p + "/" + y
        agg_yr_det = os.listdir(p2)
        for k in agg_yr_det:
            p3 = p2 + "/" + k
            data = open(p3, 'r')
            B = json.load(data)
            try:
                for v in B['data']['usersByDevice']:
                    D2["Brand"].append(v['brand'])
                    D2["count"].append(v['count'])
                    D2["Percentage"] = v['percentage']
                    D2["State"].append(i)
                    D2["Year"].append(y)
                    D2["Quarter"].append(int(k.strip('.json')))
            except:
                pass
df2 = pd.DataFrame(D2)
df2.to_csv("user_by_device.csv")

df2

# In[112]:


path = r"C:/Users/HP/phonepe_pulse/data/map/transaction/hover/country/india/state"
hover_state = os.listdir(path)
D3 = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Count': [], 'Amount': []}
for i in hover_state:
    p = path + "/" + i
    hover_yr = os.listdir(p)
    for row in hover_yr:
        M = p + "/" + row
        hover_yr = os.listdir(M)
        for k in hover_yr:
            N = M + "/" + k
            Data = open(N, 'r')
            A = json.load(Data)
            for v in A['data']['hoverDataList']:
                Name = v["name"]
                count = v["metric"][0]['count']
                amount = scientific_to_amount(v["metric"][0]['amount'])
                D3["District"].append(Name)
                D3["Count"].append(count)
                D3["Amount"].append(amount)
                D3["State"].append(i)
                D3["Year"].append(row)
                D3["Quarter"].append(int(k.strip('.json')))
df3 = pd.DataFrame(D3)
df3.to_csv("map_trans.csv")
df3

# In[7]:


path = "C:/Users/HP/phonepe_pulse/data/map/user/hover/country/india/state"
hover_state = os.listdir(path)
D4 = {'State': [], 'Year': [], 'Quarter': [], 'Users': [], 'Districts': [], 'App_opens': []}
for i in hover_state:
    p = path + "/" + i
    hover_yr = os.listdir(p)
    for row in hover_yr:
        M = p + "/" + row
        hover_yr = os.listdir(M)
        for k in hover_yr:
            N = M + "/" + k
            Data = open(N, 'r')
            A = json.load(Data)
            for district, values in A['data']['hoverData'].items():
                users = values['registeredUsers']
                AppOpens = values['appOpens']
                d = district
                D4["Users"].append(users)
                D4['App_opens'].append(AppOpens)
                D4["Districts"].append(d)
                D4["State"].append(i)
                D4["Year"].append(row)
                D4["Quarter"].append(int(k.strip('.json')))
df4 = pd.DataFrame(D4)
# df4.to_csv('map_user_state.csv')
df4

# In[42]:


# path="C:/Users/HP/phonepe_pulse/data/top/transaction/country/india/state"
# top_states=os.listdir(path)
# D5={'State':[], 'Year':[],'Quarter':[],'Districts':[], 'Count':[], 'Amount':[]}
# for i in top_states:
#     p=path+"/"+i
#     top_yr=os.listdir(p)
#     for row in top_yr:
#         M=p+"/"+row
#         top_yr_list=os.listdir(M)
#         for k in top_yr_list:
#             N=M+'/'+k
#             with open(N, 'r') as file:
#                 A=json.load(file)
#             for z in A['data']['districts']:
#                 name=z['entityName']
#                 count=z['metric']['count']
#                 amount=z['metric']['amount']
#                 D5['Districts'].append(name)
#                 D5['Count'].append(count)
#                 D5['Amount'].append(amount)
#                 D5['State'].append(i)
#                 D5['Year'].append(row)
#                 D5["Quarter"].append(int(k.strip('.json')))

# df5=pd.DataFrame(D5)
# df5.to_csv("top_transpin.csv")
# df5.head(20)


# In[8]:


# d5
path = "C:/Users/HP/phonepe_pulse/data/top/transaction/country/india/state"
top_states = os.listdir(path)
D55 = {'State': [], 'Year': [], 'Quarter': [], 'Pincode': [], 'Transaction_Count': [], 'Transaction_Amount': []}
for i in top_states:
    p = path + "/" + i
    top_yr = os.listdir(p)
    for row in top_yr:
        M = p + "/" + row
        top_yr_list = os.listdir(M)
        for k in top_yr_list:
            N = M + '/' + k
            with open(N, 'r') as file:
                A = json.load(file)
            for z in A['data']['pincodes']:
                pincode = z['entityName']
                count = z['metric']['count']
                amount = scientific_to_amount(z['metric']['amount'])
                D55['Transaction_Count'].append(count)
                D55['Transaction_Amount'].append(amount)
                D55['Pincode'].append(pincode)
                D55['State'].append(i)
                D55['Year'].append(row)
                D55["Quarter"].append(int(k.strip('.json')))
# pprint.pprint(D55)
df5_5 = pd.DataFrame(D55)
df5_5.to_csv("top_transpin5_5.csv")
df5_5.head(20)

# In[13]:


# path="C:/Users/HP/phonepe_pulse/data/top/user/country/india/state"
# top_states=os.listdir(path)
# D6={'State':[], 'Year':[],'Quarter':[],'Districts':[], 'Users':[]}
# for i in top_states:
#     p=path+"/"+i
#     top_yr=os.listdir(p)
#     for row in top_yr:
#         M=p+"/"+row
#         top_yr_list=os.listdir(M)
#         for k in top_yr_list:
#             N=M+'/'+k
#             with open(N, 'r') as file:
#                 A=json.load(file)
#             for z in A['data']['districts']:
#                 name=z['name']
#                 count=z['registeredUsers']
#                 D6['Districts'].append(name)
#                 D6['Users'].append(count)
#                 D6['State'].append(i)
#                 D6['Year'].append(row)
#                 D6["Quarter"].append(int(k.strip('.json')))

# df6=pd.DataFrame(D6)
# df6.to_csv("top_user_state.csv")
# df6


# In[14]:


nullcount6 = df6_6.isnull().sum()
nullcount6

# In[9]:


# d6
path = "C:/Users/HP/phonepe_pulse/data/top/user/country/india/state"
top_states = os.listdir(path)
D66 = {'State': [], 'Year': [], 'Quarter': [], 'Districts': [], 'Registered_user': []}
for i in top_states:
    p = path + "/" + i
    top_yr = os.listdir(p)
    for row in top_yr:
        M = p + "/" + row
        top_yr_list = os.listdir(M)
        for k in top_yr_list:
            N = M + '/' + k
            with open(N, 'r') as file:
                A = json.load(file)
            for z in A['data']['districts']:
                dname = z['name']
                reg_user = z['registeredUsers']
                D66['State'].append(i)
                D66['Year'].append(row)
                D66["Quarter"].append(int(k.strip('.json')))
                D66['Districts'].append(dname)
                D66['Registered_user'].append(reg_user)

df6_6 = pd.DataFrame(D66)
df6_6.to_csv("top_user_state.csv")
df6_6

# In[70]:


nullcount6_6 = df6_6.isnull().sum()
nullcount6_6

# In[71]:


df5_5 = df5_5.dropna()

# In[72]:


nullcount5_5 = df5_5.isnull().sum()
nullcount5_5

# In[20]:


nullcount4 = df4.isnull().sum()
nullcount4

# In[21]:


nullcount3 = df3.isnull().sum()
nullcount3

# In[22]:


nullcount2 = df2.isnull().sum()
nullcount2

# In[29]:


nullcount1 = df.isnull().sum()
nullcount1

# In[10]:


# Establish the connection
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root123',
    autocommit=True
)

# In[11]:


mycursor = connection.cursor(buffered=True)

# In[73]:


mycursor.execute("create database phonepe_db1")

# In[12]:


mycursor.execute("use phonepe_db1")

# In[115]:


query = "create table agg_transaction(state varchar(100), year int, quarter int, trans_type varchar(80), trans_count int, trans_amt double)"
mycursor.execute(query)

# In[116]:


for i, row in df1.iterrows():
    query = "insert into agg_transaction values (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query, tuple(row))
    connection.commit()

# In[117]:


query = "create table agg_user_dev(state varchar(100),year int, quarter int, brand varchar(30), count int, percentage double)"
mycursor.execute(query)

# In[120]:


for i, row in df2.iterrows():
    query = "insert into agg_user_dev values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query, tuple(row))
    connection.commit()

# In[121]:


query = "create table map_trans(state varchar(100),year int, quarter int,district varchar(100), count int, amount double)"
mycursor.execute(query)

# In[122]:


for i, row in df3.iterrows():
    query = "insert into map_trans values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query, tuple(row))
    connection.commit()

# In[13]:


query = "create table map_user(state varchar(100),year int, quarter int, Reg_users int, district varchar(100), app_open int)"
mycursor.execute(query)

# In[14]:


for i, row in df4.iterrows():
    query = "insert into map_user values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query, tuple(row))
    connection.commit()

# In[16]:


query = "create table top_transpin(state varchar(100),year int, quarter int, pincode int, transaction_count int, transaction_amount double)"
mycursor.execute(query)

# In[17]:


for i, row in df5_5.iterrows():
    query = "insert into top_transpin values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query, tuple(row))
    connection.commit()

# In[18]:


query = "create table top_user_state(state varchar(100),year int, quarter int, district varchar(80),Reg_users int)"
mycursor.execute(query)

# In[20]:


for i, row in df6_6.iterrows():
    query = "insert into top_user_state values(%s,%s,%s,%s,%s)"
    mycursor.execute(query, tuple(row))
    connection.commit()

# In[ ]:
s={'andaman-&-nicobar-islands':'Andaman & Nicobar',
   'andhra-pradesh':'Andhra Pradesh',
   'arunachal-pradesh':'Arunachal Pradesh',
    'assam':'Assam',
   'bihar':'Bihar',
   'chandigarh':'Chandigarh',
   'chhattisgarh':'Chhattisgarh',
   'dadra-&-nagar-haveli-&-daman-&-diu':'Dadra and Nagar Haveli and Daman and Diu',
   'delhi':'Delhi',
   'goa':'Goa',
   'gujarat':'Gujarat',
    'haryana':'Haryana',
   'himachal-pradesh':'Himachal Pradesh',
   'jammu-&-kashmir':'Jammu & Kashmir',
   'jharkhand':'Jharkhand',
   'karnataka':'Karnataka',
   'kerala':'Kerala',
   'ladakh':'Ladakh',
   'lakshadweep':'Lakshadweep',
   'madhya-pradesh':'Madhya Pradesh',
   'maharashtra':'Maharashtra',
   'manipur':'Manipur',
   'meghalaya':'Meghalaya',
   'mizoram':'Mizoram',
   'nagaland':'Nagaland',
   'odisha':'Odisha',
   'puducherry':'Puducherry',
   'punjab':'Punjab',
   'rajasthan':'Rajasthan',
   'sikkim':'Sikkim',
   'tamil-nadu':'Tamil Nadu',
   'telangana':'Telangana',
   'tripura':'Tripura',
   'uttar-pradesh':'Uttar Pradesh',
   'uttarakhand':'Uttarakhand',
   'west-bengal':'West Bengal'}

for df in [df1,df2,df3,df4,df5_5,df6_6]:
    df['State']=df['State'].map(s)
    print(df.columns)

####################Districts	Registered_user Testing#############################################################################33


# In[20]:


Year = 2019
Quarter = 3
mycursor.execute(
    f"select state, sum(trans_count) as Total_Transactions_Count, sum(trans_amt) as Total from agg_transaction where year = {Year} and quarter = {Quarter} group by state order by Total desc limit 10")
df = pd.DataFrame(mycursor.fetchall(), columns=['State', 'Transactions_Count', 'Total_Amount'])
fig = px.pie(df, values='Total_Amount',
             names='State',
             title='Top 10',
             color_discrete_sequence=px.colors.sequential.Agsunset,
             hover_data=['Transactions_Count'],
             labels={'Transactions_Count': 'Transaction_Count'})

fig.show()
df
# fig.update_traces(textposition='inside', textinfo='percent+label')
# st.plotly_chart(fig,use_container_width=True)


# In[ ]:


Year = 2019
Quarter = 3
mycursor.execute(f"select state,year,brand

State
Year
Quarter
Brand
count
Percentage
0
andaman - & -nicobar - islands
2018
1
Xiaomi
1665
0.100199
1
andaman - & -nicobar - islands
2018
1
Samsung
1445
0.100199
2
andaman - & -nicobar - islands
2018
1
Vivo
982
0.100199
3
andaman - & -nicobar - islands
2018
1
Oppo
501
0.100199

# In[5]:


# Sample DataFrame
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [47, 30, 20, 15, 35]
})

fig = px.pie(data, names='Category', values='Value')
fig.show()

# In[32]:


# Testing
# path="C:/Users/HP/phonepe_pulse/data/top/transaction/country/india/state"
# top_states=os.listdir(path)
# D8={'State':[], 'Year':[],'Quarter':[],'Districts':[], 'Count':[], 'Amount':[]}
# for i in top_states:
#     p=path+"/"+i
#     top_yr=os.listdir(p)
#     for row in top_yr:
#         M=p+"/"+row
#         top_yr_list=os.listdir(M)
#         for k in top_yr_list:
#             N=M+'/'+k
#             with open(N, 'r
#             ) as file:
#                 A=json.load(file)
#             for z in A['data']['districts']:
#                 name=z['entityName']
#                 count=z['metric']['count']
#                 amount=z['metric']['amount']
#                 D5['Districts'].append(name)
#                 D5['Count'].append(count)
#                 D5['Amount'].append(amount)
#                 D5['State'].append(i)
#                 D5['Year'].append(row)
#                 D5["Quarter"].append(int(k.strip('.json')))
#             for p in A['data']['pincodes']:
#                 pincode=z['entityName']

# df5=pd.DataFrame(D5)
# df5.to_csv("top_trans_state.csv")
# df5.head(20)


# In[11]:


pprint.pprint(A)

# In[31]:


for z in A['data']['pincodes']:
    pprint.pprint(z['entityName'])

# In[13]:


fig = px.bar(df6_6, x='State', y='Registered_user')
fig.show()

# In[34]:


pprint.pprint(A)

# In[77]:


df1['Transaction_amount']

# In[107]:


def scientific_to_amount(scientific_notation):
    # Convert scientific notation to a float
    number = float(scientific_notation)

    # Format the float as a string with two decimal places
    formatted_amount = '{:.2f}'.format(number)

    return formatted_amount


# In[108]:


Test1 = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [],
         'Transaction_amount': []}
for i in Agg_state:
    p = path + "/" + i
    Agg_yr = os.listdir(p)
    for y in Agg_yr:
        M = p + "/" + y
        Agg_yr_list = os.listdir(M)

        for k in Agg_yr_list:
            N = M + "/" + k
            Data = open(N, 'r')
            A = json.load(Data)
            for v in A['data']['transactionData']:
                Name = v["name"]
                count = v["paymentInstruments"][0]['count']
                amount = scientific_to_amount(v["paymentInstruments"][0]['amount'])
                Test1["Transaction_type"].append(Name)
                Test1["Transaction_count"].append(count)
                Test1["Transaction_amount"].append(amount)
                Test1["State"].append(i)
                Test1["Year"].append(y)
                Test1["Quarter"].append(int(k.strip('.json')))
dfTest1 = pd.DataFrame(Test1)
# df1.to_csv('Agg_trans1.csv')
dfTest1



