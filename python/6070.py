#!/usr/bin/env python
# coding: utf-8

# In[117]:
'''
월이 입력될 때 계절 이름이 출력되도록 해보자.

월 : 계절 이름
12, 1, 2 : winter
  3, 4, 5 : spring
  6, 7, 8 : summer
  9, 10, 11 : fall




'''

a=input()
a=int(a)
if a==12 or a==1 or a==2:
    print("winter")
elif a==3 or a==4 or a==5:
    print("spring")
elif a==6 or a==7 or a==8:
    print("summer")
else :
    print("fall")


# In[ ]:




