#!/usr/bin/env python
# coding: utf-8

# # nb

# In[1]:


import plotly.express as px
data = px.data.iris()
data.head()


# In[2]:


import altair as alt
alt.Chart(data=data).mark_point().encode(
    x="sepal_width",
    y="sepal_length",
    color="species",
    size='sepal_length'
)


# In[ ]:




