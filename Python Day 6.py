#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

# Membaca data dengan header
df_radiosonde = pd.read_csv(r'D:\Clean_D96935_2019010112.csv') 

# Merapikan header data
df_radiosonde.columns = [x.strip() for x in df_radiosonde.columns] 
df_radiosonde.info()


# In[10]:


contohdata = 'https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/property_data.csv'
df = pd.read_csv(contohdata)
df.head(10)


# In[16]:


# Standar missing value
df['ST_NUM']
print(df['ST_NUM'].isnull())
print('Data yang salah adalah:', df['ST_NUM'].isnull().sum())


# In[17]:


#Missing value tidak standar
df['NUM_BEDROOMS']
print(df['NUM_BEDROOMS'].isnull())
print('Data yang salah adalah: ', df['NUM_BEDROOMS'].isnull().sum())


# In[20]:


missing_values = ['n/a', 'na', '--']
df = pd.read_csv(contohdata, na_values = missing_values)
df['NUM_BEDROOMS'].isnull()
print(df['NUM_BEDROOMS'].isnull())
print('Data yang salah adalah: ', df['NUM_BEDROOMS'].isnull().sum())


# In[22]:


data = pd.ExcelFile('D:/obes.xls')
data.sheet_names


# In[24]:


# Cek data error
missingvalue = ['-----']
df_radiosondeclean = pd.read_csv(r'D:\Clean_D96935_2019010112.csv', na_values = missingvalue)
print(df_radiosondeclean['Humi0'].isnull().sum())

df_radiosondeclean.columns = [x.strip() for x in df_radiosondeclean.columns]

df_radiosondeclean['Temp0'].plot(label = 'Tekanan', legend = True)
df_radiosondeclean['Press0'].plot(label = 'Tekanan', legend = True)
df_radiosondeclean['Humi0'].plot(label = 'Humiditas', legend = True)


# In[31]:


from datetime import datetime
date_rng = pd.date_range(start = '19:00:00', end = '19:23:00', freq = 'T')
date_rng


# In[36]:


# df = df_radiosondeclean.groupby(date_rng)
df = pd.DataFrame(date_rng, columns = ['date'])
df['data'] = np.random.randint(0, 100, size = (len(date_rng)))
df.head()


# In[38]:


opsd_daily = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/opsd_germany_daily.csv', index_col = 0, parse_dates = True)
opsd_daily.head()


# In[40]:


opsd_daily['Year'] = opsd_daily.index.year
opsd_daily['Month'] = opsd_daily.index.month
opsd_daily['Weekday'] = opsd_daily.index.weekday
opsd_daily.head()
# plotting
opsd_daily['Consumption'].plot(linewidth = 0.5)


# In[68]:


opsd_daily['Consumption'].plot(marker = '+', alpha = 0.5, linestyle = 'None', figsize = (11,9))


# In[70]:


# Boxplot
opsd_daily.boxplot(column = ['Consumption'], by = 'Month')

