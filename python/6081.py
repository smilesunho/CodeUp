#!/usr/bin/env python
# coding: utf-8

# In[41]:
'''
A, B, C, D, E, F 중 하나가 입력될 때,
1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
(단, A ~ F 까지만 입력된다.)
'''

n=input()
n=int(n,16)
for i in range(1,16):
    print('%X'%n,'*%X'%i,'=%X'%(n*i),sep='')
    
        



# In[ ]:





# In[ ]:




