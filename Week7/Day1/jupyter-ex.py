#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1
import numpy as np 


# In[2]:


# 2
np.zeros(10)


# 4) The memory size in Bytes required by an rectangular array is (# of rows)(# of cols)(size of one element).

# 5) Python has a built-in help() function that can access this information and prints the results. For example, to see the documentation of the built-in len function, you can do the following: In [1]: help(len) Help on built-in function len in module builtins: len(...)

# In[3]:


# 6
v = np.zeros(10)
v[4] = 1
print(v)


# In[11]:


# 7
z = np.arange(10,50)
print(z)

# 8
x = z[::-1]
print(x)


# In[14]:


# 9
w = np.arange(9).reshape(3,3)
print (w)

# 10
np.nonzero([1,2,0,0,4,0])


# In[21]:


# 11
y = np.eye(3)
print (y)


# In[26]:


# 12
z = np.random.uniform((3,3,3))
print (z)


# In[28]:


# 13
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)


# In[18]:


# 14
Z = np.random.random(10)
m = Z.mean()
print (m)


# In[41]:


# 15
Z = np.ones((10,10))
Z[1:-1,1:-1]=0
print(Z)

# 16
x = np.ones((3,3))
y = np.pad(x,pad_width=1)
print(y)

# 17
print(0 * np.nan)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)


# In[44]:


# 18
Z = np.diag([1,2,3,4,7])
print (Z)


# In[58]:


# 19
Z = np.zeros ((8,8), dtype=int)
Z[1::2, ::2]= 1
Z[::2, 1::2] = 1
print (Z)

# 20
print (np.unravel_index(100, (6,7,8)))


# In[51]:


# 21
array= np.array([[0,1], [1,0]])
Z = np.tile(array,(4,4))
print (Z)


# In[50]:


# 22
Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z= (Z-Zmin)/(Zmax-Zmin)
print (Z)


# In[69]:


# 23
arr = np.array([2,4],dtype = np.int16)
print(arr.dtype)


# In[60]:


# 24
Z= np.dot(np.ones((5,3)), np.ones((3,2)))
print (Z)


# In[75]:


# 25
Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print(Z)


# In[87]:


# 26
print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))


# In[92]:


# 27
Z <- Z
1j*Z


# In[94]:


# 28
np.array(0)


# In[96]:


# 29
# we ceate an array
# use np.round


# In[ ]:


# 30
# we use mean


# In[1]:


np.array(0)


# In[ ]:





# In[ ]:




