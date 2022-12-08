#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import ssl


# In[23]:


chipo = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv', sep = '\t')


# In[24]:


chipo.head(10)


# In[26]:


rows_count = len(chipo.index)
print(rows_count)


# In[27]:


columns_count = len(chipo.columns)
print(columns_count)


# In[29]:


# chipo.shape


# In[30]:


list(chipo.columns)


# In[31]:


chipo.index


# In[36]:


a = chipo.groupby('item_name')
a = a.sum()
a = a.sort_values(['quantity'], ascending = False)
a.head(1)


# In[40]:


total_items_ordered = chipo.quantity.sum()
print(total_items_ordered)


# In[41]:


print('For the most-ordered item, ordered were:',str(713926))


# In[42]:


b = chipo.groupby('choice_description').sum()
b = b.sort_values(['quantity'], ascending = False)
b.head(2)


# In[43]:


total_items_ordered = chipo.quantity.sum()
total_items_ordered


# In[44]:


chipo.item_price.dtype


# In[47]:


dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)
 


# In[48]:


chipo.item_price.dtype


# In[49]:


a


# In[50]:


revenue = (chipo['quantity'] * chipo['item_price']).sum()

print('Revenue was: $' + str(np.round(revenue,2)))


# In[51]:


orders = chipo.order_id.value_counts().count()
orders


# In[ ]:




