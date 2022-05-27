#!/usr/bin/env python
# coding: utf-8

# In[61]:
'''
일차 방정식의 ax±b=c의 식을 입력받는다.

x의 값을 소숫점 둘째자리까지 출력하시오.
'''

v,c=input().split("=")
a,b=v.split("x")
a=int(a)
b=int(b)
c=int(c)
b=b*(-1)
k=(b+c)/a
print('{0:0.2f}'.format(k))


# In[ ]:




