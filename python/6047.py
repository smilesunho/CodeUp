#!/usr/bin/env python
# coding: utf-8

# In[25]:
'''
정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
'''

a,b=input().split(" ")
a=int(a)
b=int(b)
c=2**b
print(a*c)

