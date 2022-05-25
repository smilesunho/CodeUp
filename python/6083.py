#!/usr/bin/env python
# coding: utf-8

# In[32]:

'''
만들 수 있는 rgb 색의 정보를 오름차순(계단을 올라가는 순, 12345... abcde..., 가나다라마...)으로
줄을 바꿔 모두 출력하고, 마지막에 그 개수를 출력한다.
 


'''

a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
for i in range(0,a):
    for k in range(0,b):
        for t in range(0,c):
            print(i,k,t)
print(a*b*c)


# In[ ]:




