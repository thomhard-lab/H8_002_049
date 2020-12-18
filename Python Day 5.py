#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd


# In[7]:


# data_frame = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/nbaallelo.csv')


# In[ ]:


len(data_frame)


# In[5]:


# Membaca data dengan header
df_radiosonde = pd.read_csv(r'D:\Clean_D96935_2019010112.csv') 


# In[6]:


# menampilkan data
df_radiosonde.head()


# In[8]:


# untuk mengetahui banyaknya data
print(df_radiosonde.shape)


# In[9]:


# Membaca data tanpa header
df_radiosonde2 = pd.read_csv(r'D:\Dirty_D96935_2019010112.csv',header = None) 


# In[10]:


# menampilkan 5 data pertama
df_radiosonde2.head()


# In[21]:


# menampilkan 5 data terakhir
df_radiosonde.tail()


# In[52]:


pd.set_option("display.precision", 5)


# In[53]:


pd.set_option("display.max.columns", None)


# In[22]:


# menampilkan info dari data
df_radiosonde.info()


# In[26]:


# Mengubah tanggal
# df_kolom1 = pd.to_datetime(df_radiosonde[1,])


# In[23]:


# menampilkan nilai hasil statistika dasar
df_radiosonde.describe()


# In[38]:


df_radiosonde[' ObsTime'].value_counts()'


# In[58]:


# locate data
Suhu_panas = df_radiosonde['Temp0'] >= 25
df_radiosonde.loc[Suhu_panas]

Suhu_dingin = df_radiosonde['Temp0'] < 25
df_radiosonde.loc[Suhu_dingin]


# In[61]:


# Merapikan header data
df_radiosonde.columns = [x.strip() for x in df_radiosonde.columns] 
df_radiosonde.info()


# In[62]:


df_radiosonde.keys()


# In[66]:


# Mengecek index header
'T0' in df_radiosonde


# In[78]:


df_radiosonde.iloc[1:3]


# In[88]:


# locate data
Suhu_panas = df_radiosonde['Temp0'] >= 25
df_radiosonde.loc[Suhu_panas]

Suhu_dingin = df_radiosonde['Temp0'] < 25
df_radiosonde.loc[Suhu_dingin]

Suhu_sedang = (df_radiosonde['Temp0'] > 25) & (df_radiosonde['Temp0'] < 35)
df_radiosonde.loc[Suhu_sedang]


# In[92]:


# group by
df_radiosonde[Suhu_sedang].groupby(['PDP']).max()


# In[103]:


city_data = pd.DataFrame(
{'revenue': [4200, 6500, 8000], 'employee_count': [5, 8, 'NaN']},
index = ['Amsterdam', 'Tokyo', 'Toronto'])
city_data


# In[105]:


further_city_data = pd.DataFrame(
{'revenue': [7000, 3400], 'employee_count': [2, 2]},
index = ['New York', 'Barcelona'])
further_city_data


# In[109]:


# Combine Dataset
all_city_data = pd.concat([city_data, further_city_data], sort = False)
all_city_data


# In[125]:


df_suhu = df_radiosonde[['ObsTime', 'Temp0']]
Suhu_normal = (df_suhu['Temp0'] > 25) & (df_suhu['Temp0'] < 35)
df_suhu[Suhu_normal].groupby(['ObsTime']).mean().plot()


# In[126]:


df_suhu[Suhu_normal].groupby(['ObsTime']).mean().plot(kind = 'bar')


# In[ ]:




