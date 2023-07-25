#!/usr/bin/env python
# coding: utf-8

# # Set 4

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import seaborn as sns


# In[11]:


get_ipython().system('pip install statsmodels')


# In[15]:


import statsmodels.api as smf


# In[14]:


import warnings
warnings.filterwarnings('ignore')


# In[ ]:


Q3


# In[17]:


mean = 50
std = 40
n = 100
d_f = 100 - 1 #degree of freedom
#the probability that there will be an investigation,
#if the mean transactions amount increases more than 55 USD or less than 45 USD
# no investigation if the mean transactions amount remains between 45 to 55 USD

# we will go for t-distribution as population standard deviation is unknown
t_forty_five = (45-50)/(40/np.sqrt(100))

t_fifty_five = (55-50)/(40/np.sqrt(100))

forty_five = stats.t.cdf(t_forty_five, df = d_f)

fifty_five = stats.t.cdf(t_fifty_five, d_f)

prob = fifty_five - forty_five

np.round(stats.t.interval(alpha = prob, df = d_f, loc = mean, scale = std/np.sqrt(n)),)

print('The probability that in any given week, there will be an investigation is',np.round((1-prob)*100,1),'%')


# In[ ]:


# Q4


# In[18]:


x_bar = 45
s_std = 40
mew = 50

t = np.round(stats.t.ppf(0.025, df = 249),2)
t

# t_value = (x_bar - mew)/(sample_std/n**0.5)
# t = 45-50 or z = 55-50 z = +/- 5

# t = 5/(40/n**0.5)
# n = (sample_standard_deviation*tscore)/(sample_mean=population_mean)
n = ((s_std*abs(t)) / (5))**2

print('The Auditors would like to maintain the probability of investigation to 5%, they should sample',np.round(n,),'transactions if they do not want to change the thresholds of 45 to 55')

df= n-1
print(n, df)

np.round(stats.t.interval(alpha = 0.95, df = df, loc = mew, scale = s_std/np.sqrt(n)),)


# In[ ]:




