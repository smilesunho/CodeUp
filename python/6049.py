#!/usr/bin/env python
# coding: utf-8

# In[28]:
'''
두 정수(a, b)를 입력받아
a와 b의 값이 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.
'''

a,b=input().split(" ")
a=int(a)
b=int(b)
if a==b:
    print("True")
else :
    print("False")

