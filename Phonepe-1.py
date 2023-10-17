#!/usr/bin/env python
# coding: utf-8

# In[24]:


import requests
import os
import json
import pprint
import pandas as pd
import git
import mysql.connector


# In[3]:


repository_url = "https://github.com/phonepe/pulse.git"
local_directory = "phonepe_pulse"
git.Repo.clone_from(repository_url, local_directory)


# In[4]:


os.listdir("C:\\Users\\HP\\phonepe_pulse\\.git")


# In[5]:


import pandas as pd


path="C:/Users/HP/phonepe_pulse/data/aggregated/transaction/country/india/state"
Agg_state=os.listdir(path)


Agg_state


# In[6]:


D1={'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in Agg_state:
    p=path+"/"+i
    Agg_yr=os.listdir(p) 
    for y in Agg_yr:
        M=p+"/"+y
        Agg_yr_list=os.listdir(M)

        for k in Agg_yr_list:
            N=M+"/"+k
            Data=open(N,'r')
            A=json.load(Data)
            for v in A['data']['transactionData']:
                   Name=v["name"]
                   count=v["paymentInstruments"][0]['count']
                   amount=v["paymentInstruments"][0]['amount']
                   D1["Transaction_type"].append(Name)
                   D1["Transaction_count"].append(count)
                   D1["Transaction_amount"].append(amount)
                   D1["State"].append(i)
                   D1["Year"].append(y)
                   D1["Quarter"].append(int(k.strip('.json')))
df=pd.DataFrame(D1)
df.to_csv('Agg_trans.csv')


# In[7]:


df


# In[8]:


path="C:/Users/HP/phonepe_pulse/data/aggregated/user/country/india/state"
D2={'State':[], 'Year':[],'Quarter':[],'Brand':[], 'count':[], 'Percentage':[]}
Agg_state=os.listdir(path)
for i in Agg_state:
    p=path+"/"+i
    agg_yr=os.listdir(p)
    for y in agg_yr:
        p2=p+"/"+y
        agg_yr_det=os.listdir(p2)
        for k in agg_yr_det:
            p3=p2+"/"+k
            data=open(p3,'r')
            B=json.load(data)
            try:
                for v in B['data']['usersByDevice']:
                    D2["Brand"].append(v['brand'])
                    D2["count"].append(v['count'])
                    D2["Percentage"]=v['percentage']
                    D2["State"].append(i)
                    D2["Year"].append(y)
                    D2["Quarter"].append(int(k.strip('.json')))
            except:
                pass
df2=pd.DataFrame(D2)
df2.to_csv("user_by_device.csv") 
    
df2


# In[9]:


path=r"C:/Users/HP/phonepe_pulse/data/map/transaction/hover/country/india/state"
hover_state=os.listdir(path)
D3={'State':[], 'Year':[],'Quarter':[],'District':[], 'Count':[], 'Amount':[]}
for i in hover_state:
    p=path+"/"+i
    hover_yr=os.listdir(p)
    for row in hover_yr:
        M=p+"/"+row
        hover_yr=os.listdir(M)
        for k in hover_yr:
            N=M+"/"+k
            Data=open(N,'r')
            A=json.load(Data)
            for v in A['data']['hoverDataList']:
                   Name=v["name"]
                   count=v["metric"][0]['count']
                   amount=v["metric"][0]['amount']
                   D3["District"].append(Name)
                   D3["Count"].append(count)
                   D3["Amount"].append(amount)
                   D3["State"].append(i)
                   D3["Year"].append(row)
                   D3["Quarter"].append(int(k.strip('.json')))
df3=pd.DataFrame(D3)
df3.to_csv("map_trans.csv")
df3   


# In[10]:


path="C:/Users/HP/phonepe_pulse/data/map/user/hover/country/india/state"
D4={'State':[], 'Year':[],'Quarter':[],'Users':[], 'Districts':[],'App_opens':[]}
for i in hover_state:
    p=path+"/"+i
    hover_yr=os.listdir(p) 
    for row in hover_yr:
        M=p+"/"+row
        hover_yr=os.listdir(M)
        for k in hover_yr:
            N=M+"/"+k
            Data=open(N,'r')
            A=json.load(Data)
            for district,values in A['data']['hoverData'].items():
                   users=values['registeredUsers']
                   AppOpens=values['appOpens']
                   d=district
                   D4["Users"].append(users)
                   D4['App_opens'].append(AppOpens)
                   D4["Districts"].append(d)
                   D4["State"].append(i)
                   D4["Year"].append(row)
                   D4["Quarter"].append(int(k.strip('.json')))
df4=pd.DataFrame(D4)
df4.to_csv('map_user_state.csv')
df4


# In[11]:


path="C:/Users/HP/phonepe_pulse/data/top/transaction/country/india/state"
top_states=os.listdir(path)
D5={'State':[], 'Year':[],'Quarter':[],'Districts':[], 'Count':[], 'Amount':[]}
for i in top_states:
    p=path+"/"+i
    top_yr=os.listdir(p)    
    for row in top_yr:
        M=p+"/"+row
        top_yr_list=os.listdir(M)        
        for k in top_yr_list:
            N=M+'/'+k
            with open(N, 'r') as file:
                A=json.load(file)
            for z in A['data']['districts']:
                name=z['entityName']
                count=z['metric']['count']
                amount=z['metric']['amount']
                D5['Districts'].append(name)
                D5['Count'].append(count)
                D5['Amount'].append(amount)
                D5['State'].append(i)
                D5['Year'].append(row)
                D5["Quarter"].append(int(k.strip('.json')))

df5=pd.DataFrame(D5)
df5.to_csv("top_trans_state.csv")
df5.head(20)


# In[13]:


path="C:/Users/HP/phonepe_pulse/data/top/user/country/india/state"
top_states=os.listdir(path)
D6={'State':[], 'Year':[],'Quarter':[],'Districts':[], 'Users':[]}
for i in top_states:
    p=path+"/"+i
    top_yr=os.listdir(p)    
    for row in top_yr:
        M=p+"/"+row
        top_yr_list=os.listdir(M)        
        for k in top_yr_list:
            N=M+'/'+k
            with open(N, 'r') as file:
                A=json.load(file)
            for z in A['data']['districts']:
                name=z['name']
                count=z['registeredUsers']
                D6['Districts'].append(name)
                D6['Users'].append(count)
                D6['State'].append(i)
                D6['Year'].append(row)
                D6["Quarter"].append(int(k.strip('.json')))

df6=pd.DataFrame(D6)
df6.to_csv("top_user_state.csv")
df6


# In[18]:


nullcount6=df6.isnull().sum()
nullcount6


# In[19]:


nullcount5=df5.isnull().sum()
nullcount5


# In[20]:


nullcount4=df4.isnull().sum()
nullcount4


# In[21]:


nullcount3=df3.isnull().sum()
nullcount3


# In[22]:


nullcount2=df2.isnull().sum()
nullcount2


# In[29]:


nullcount1=df.isnull().sum()
nullcount1


# In[25]:


# Establish the connection
connection = mysql.connector.connect(
                                        host = 'localhost',
                                        user = 'root',
                                        password = 'root123',
                                        autocommit=True
                                    )


# In[26]:


mycursor = connection.cursor(buffered=True)


# In[27]:


mycursor.execute("create database phonepe_db1")


# In[30]:


mycursor.execute("use phonepe_db1")
query="create table agg_transaction(state varchar(50), year int, quarter int, trans_type varchar(80), trans_count int, trans_amt double)"
mycursor.execute(query)


# In[42]:


for i,row in df.iterrows():
    query="insert into agg_transaction values (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,tuple(row))
    connection.commit()


# In[43]:


query="create table agg_user_dev(state varchar(50),year int, quarter int, brand varchar(30), count int, percentage double)"
mycursor.execute(query)


# In[44]:


for i,row in df2.iterrows():
    query="insert into agg_user_dev values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,tuple(row))
    connection.commit()


# In[45]:


query="create table map_trans(state varchar(50),year int, quarter int,district varchar(60), count int, amount double)"
mycursor.execute(query)


# In[47]:


for i,row in df3.iterrows():
    query="insert into map_trans values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,tuple(row))
    connection.commit()


# In[49]:


query="create table map_user(state varchar(50),year int, quarter int, Reg_users int, district varchar(80), app_open int)"
mycursor.execute(query)


# In[50]:


for i,row in df4.iterrows():
    query="insert into map_user values(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(query,tuple(row))
    connection.commit()


# In[ ]:




