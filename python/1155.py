#!/usr/bin/env python
# coding: utf-8

# In[10]:


'''
인학이는 숫자 7을 좋아한다.

어떤 정수가 입력되면 그 수가 7의 배수인지 확인하시오.
'''
a=input()
a=int(a)
if a%7==0:
    print("multiple")
else:
    print("not multiple")

