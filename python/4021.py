#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''
7개의 자연수가 주어질 때, 이들 중 홀수인 자연수들을 모두 찾아 그 합을 구하는 프로그램을 작성하시오.
홀수가 없다면 -1을 출력하시오
'''
a=list(map(int,input().strip().split(" ")))
b=[]
for i in a:
    if i%2!=0:
        b.append(i)
if len(b)==0:
    print("-1")
else:
    print(sum(b))
        


# In[ ]:




