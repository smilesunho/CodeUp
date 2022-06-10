#!/usr/bin/env python
# coding: utf-8

# In[21]:


'''
시작값과 마지막값이 입력되면 그 두 수 사이의 소수를 모두 출력하시오.
'''
a,b=input().split(" ")
a=int(a)
b=int(b)
def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:          
            for j in range(i+i, n, i): 
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

x=prime_list(b+1)

for i in x:
    if i>=a:
        print(i,end=" ")


# In[ ]:




