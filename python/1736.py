#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
초를 입력받아 일 / 시 / 분 / 초의 형태로 나타내시오.

'''
a=input()
a=int(a)
b=a//86400
c=a%86400
d=c//3600
e=c%3600
f=e//60
g=e%60

print(b, d, f, g)

