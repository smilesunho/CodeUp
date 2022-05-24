#!/usr/bin/env python
# coding: utf-8

# In[59]:
"""
2개의 정수값이 입력될 때,
그 불 값(True/False) 이 서로 다를 때에만 True 를 출력하는 프로그램을 작성해보자.

"""

a, b = input().split()
a=bool(int(a))
b=bool(int(b))
if a==True and b==True:
    print("False")
elif a==False and b==False:
    print("False")
else :
    print("True")


# In[ ]:




