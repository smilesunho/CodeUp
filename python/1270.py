#!/usr/bin/env python
# coding: utf-8

# In[20]:


'''
어떤 수 n이 주어지면 1부터 n까지의 수 중 
맨 마지막 자리에 1이 몇 번 들어 있는지 알아내는 프로그램을 작성하시오.
'''
a=input()
a=int(a)
b=[]
for i in range(1,a+1):
    k=str(i)
    j=len(k)-1
    if k[j]=='1':
        b.append(k)
print(len(b))

      

        


