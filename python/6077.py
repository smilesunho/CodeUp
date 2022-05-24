#!/usr/bin/env python
# coding: utf-8

# In[145]:
'''
정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.


'''

a=input()
a=int(a)
b=0
for i in range (0,a+1):
    if i%2==0:
        b=b+i
print(b)
        


# In[ ]:




