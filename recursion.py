#!/usr/bin/env python
# coding: utf-8

# In[24]:


def fibonnaci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonnaci(n-1) + fibonnaci(n-2)


# In[25]:


def gcd(a, b):  
    while b:
        (a, b) = (b, (a % b))
    return a


# In[26]:


def compareTo(s1, s2):
    if len(s1) == len(s2):
        return int(0)
    elif len(s1) < len(s2):
        return int(-1)
    elif len(s1) > len(s2):
        return int(1)

