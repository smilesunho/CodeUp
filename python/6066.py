#!/usr/bin/env python
# coding: utf-8

# In[85]:
#3개의 정수(a, b, c)가 입력되었을 때, 짝(even)/홀(odd)을 출력해보자.

a, b, c = input().split()
e=int(a)%2
f=int(b)%2
g=int(c)%2
d=[e,f,g]
for i in range(0,3):
    if d[i]==0:
        print ("even")
    else :
        print ("odd")



# In[ ]:




