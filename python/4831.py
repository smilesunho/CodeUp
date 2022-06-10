#!/usr/bin/env python
# coding: utf-8

# In[7]:


'''
첫 줄에는 날짜의 일의 자리 숫자가 주어지고, 두 번째 줄에는 5대의 자동차 번호의 일의 자리 숫자가 주어진다. 날짜와 자동차의 일의 자리 숫자는 모두 0에서 9까지의 정수 중 하나이다.
주어진 날짜와 자동차의 일의 자리 숫자를 보고 10부제를 위반하는 차량의 대수를 출력한다.
'''
a=input()
a=int(a)
b=input().strip().split(" ")
z=[]
for i in b:
    if a==int(i):
        z.append(a)
print(len(z))
        
        


# In[ ]:




