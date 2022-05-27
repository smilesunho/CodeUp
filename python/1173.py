#!/usr/bin/env python
# coding: utf-8

# In[76]:
'''
공백을 기준으로 시간과 분이 주어진다.

그러면 이 시간을 기준으로 30분전의 시간을 출력하시오.

예)

12 35  =====> 12 5

12 0 ======> 11 30

11 5 ======> 10 35

'''

a,b=input().split(" ")
a=int(a)
b=int(b)
if (b-30) < 0:
    if a-1>0:
        print(a-1, 60+(b-30))
    elif a-1==0:
        print('0',60+(b-30))
    else :
        print('23',60+(b-30))
else:
    print(a, b-30)
    


# In[ ]:




