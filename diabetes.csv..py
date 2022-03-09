#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


raw_data=pd.read_csv(r"C:\Users\aryas\Downloads\diabetes.csv")


# In[3]:


raw_data.head()


# In[4]:


raw_data.tail()


# In[5]:


raw_data.describe()


# In[6]:


raw_data.info()


# In[7]:


raw_data.shape


# In[8]:


raw_data.count()


# In[10]:


raw_data["BloodPressure"].value_counts()


# In[12]:



#mean
mean_data = raw_data["BloodPressure"].mean()
print(mean_data )


# In[14]:


max_data=raw_data["BloodPressure"].max()
print(max_data)


# In[15]:


raw_data.describe(include=['object'])



# In[16]:


raw_data.describe(include=['object','float'])


# In[17]:


raw_data.isnull()


# In[18]:


raw_data.isnull().sum()


# In[19]:


# Filling missing value using fillna()
raw_data.fillna(0)


# In[20]:


raw_data.fillna(0).head()


# In[30]:


raw_data['Outcome'].fillna("0", inplace=True)


# In[31]:


raw_data


# In[33]:


# not zero in all columns
raw_data.drop(['BloodPressure'],axis=1,inplace=True)


# In[34]:


raw_data


# In[36]:


raw_data.duplicated().sum()


# In[37]:


raw_data['BMI'].duplicated().sum()


# In[39]:


raw_data.dropna()


# In[40]:


raw_data.dropna(axis=0,inplace=True)


# In[41]:


raw_data.describe()


# In[42]:


raw_data['name']=raw_data['name'].str.upper()


# In[43]:


raw_data


# In[45]:


raw_data.rename(columns={'name':'NAME'},inplace=True)


# In[46]:


raw_data


# In[47]:


raw_data.groupby(['NAME']).groups


# In[48]:


raw_data.groupby(['NAME']).head()


# In[50]:


raw_data.groupby(['NAME']).count()


# In[51]:


raw_data.groupby(['NAME']).max()


# In[52]:


raw_data.groupby(['NAME']).sum()


# In[53]:


raw_data.groupby(['NAME','BMI','Insulin','Pregnancies']).count()


# In[ ]:




