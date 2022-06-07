#!/usr/bin/env python
# coding: utf-8

# In[3]:


#두 점 간의 거리를 소수점 2째 자리까지 출력 (소수점 아래 3째 자리에서 반올림)

a,b=input().split(" ")
c,d=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=(d-b)
f=(c-a)
h=(e*e+f*f)**(0.5)
print("{:.2f}".format(h))



