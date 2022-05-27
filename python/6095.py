#!/usr/bin/env python
# coding: utf-8

# In[48]:

'''
바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.

'''

d=[]                        
for i in range(20) :
    d.append([])        
    for j in range(20) : 
        d[i].append(0)   

a=int(input())
for i in range(a):
    x, y = map(int, input().split())
    d[int(x)][int(y)] = 1
for i in range(1,20):
    for j in range(1,20):
            print(d[i][j], end = ' ')
    print()
    


    
    


# In[ ]:




