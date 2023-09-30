#!/usr/bin/env python
# coding: utf-8

# In[1]:


print('hello ml')


# In[2]:


# load data 'housing.csv' using pandas
import pandas

def load_housing_data(csv_path='housing.csv'):
    return pandas.read_csv(csv_path)

housing = load_housing_data()
housing.head()


# In[3]:


# get description of data: we have ~20640 instances in the dataset
housing.info()


# In[4]:


# find out the available categroies of ocean_proximity
housing["ocean_proximity"].value_counts()


# In[5]:


# give us a summary of the numerical attributes
housing.describe()


# In[8]:


# this will give us a better feel of the data type we are dealing with
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plot

housing.hist(bins=50, figsize=(20, 15))
plot.show()


# In[ ]:




