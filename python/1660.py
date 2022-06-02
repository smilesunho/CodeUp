#!/usr/bin/env python
# coding: utf-8

# In[51]:
'''
정수와 컴마로 이루어진 문자열이 공백없이 입력된다.(최대길이 100글자)
컴마(,)를 분리한 결과를 출력한다.
'''


a=list(input())
k=[]
for i in range(0,len(a)):
    if a[i]!=",":
        k.append(a[i])
    else:
        k.append(" ")
k.append(" ")


for i in range(0,len(k)):
    print(k[i],sep='',end='')


# In[ ]:




