#!/usr/bin/env python
# coding: utf-8

# In[39]:
'''
번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.

출석을 부른 번호 중에 가장 빠른 번호를 출력한다.

'''

a=input()
a=int(a)
b=[]
k=[]
b=input().split(" ")
for i in range(0,a):
    k.append(int(b[i]))
e=sorted(k)
print(e[0])       


# In[ ]:




