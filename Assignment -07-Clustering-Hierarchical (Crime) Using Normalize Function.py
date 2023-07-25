#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering


# In[3]:


# importing Data

data=pd.read_csv("C:/Users/Shubham Tiwari/Downloads/crime_data.csv")
data.head()


# In[4]:


data.drop(["Unnamed: 0"],axis=1,inplace=True)


# In[5]:


data.shape


# In[6]:


data.info()


# In[7]:


data.describe()


# In[8]:


data[data.duplicated()]


# In[9]:


type(data)


# In[10]:


plt.figure(figsize = (16, 10));
dendrogram = sch.dendrogram(sch.linkage(data, method='average'))


# In[11]:


# Agglomerative Clustering

hc = AgglomerativeClustering(n_clusters=5, affinity = 'euclidean', linkage = 'average')


# In[12]:


# save clusters for chart
y_hc = hc.fit_predict(data)
Clusters=pd.DataFrame(y_hc,columns=['Clusters'])
Clusters.head()


# In[13]:


data1 = pd.concat([data,Clusters], axis=1)
data1.head()


# In[14]:


data1.sort_values("Clusters").head()


# In[ ]:





# In[ ]:




