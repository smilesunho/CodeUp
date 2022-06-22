#!/usr/bin/env python
# coding: utf-8

# In[12]:


'''
9개의 서로 다른 자연수가 주어질 때, 이들 중 최대값을 찾고 그 최대값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
예를 들어, 서로 다른 9개의 자연수
3, 29, 38, 12, 57, 74, 40, 85, 61
이 주어지면 이들 중 최대값은 85이고, 이 값은 8번째 수이다.
'''
import numpy as np
i=0
b=[]
while i<9:
    a=input()
    a=int(a)
    b.append(a)
    i=i+1
k=1
c=np.max(b)
for j in b:
    if j==c:
        print(c)
        print(k)
    else:
        k=k+1
        


# In[ ]:




