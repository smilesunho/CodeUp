#!/usr/bin/env python
# coding: utf-8

# In[39]:

'''
1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
나올 수 있는 모든 경우를 출력해보자.

'''



a,b=input().split(" ")
a=int(a)
b=int(b)
for i in range(1,a+1):
    for k in range(1,b+1):
        print(i, k)
        



# In[ ]:





# In[ ]:




