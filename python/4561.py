#!/usr/bin/env python
# coding: utf-8

# In[70]:


'''
첫 째 줄부터 일곱 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100보다 작다.
홀수가 존재하는 경우 첫째 줄에 홀수들의 합을 출력하고, 둘째 줄에 홀수들 중 최소값을 출력한다.  
   
'''
z=[]
b=[]
for i in range(0,7):
    a=int(input())
    z.append(a)

for k in z:
    if k%2==0:
        pass
    else:
        b.append(k)
        
print(sum(b))
print(min(b))
        

    
    
    


# In[ ]:




