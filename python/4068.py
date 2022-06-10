#!/usr/bin/env python
# coding: utf-8

# In[62]:


'''
소수(prime number)란 약수가 1과 자기 자신 뿐인 1보다 큰 자연수로 정의된다.

소수를 작은 수에서 큰 수 순서로 나열해 보면 2,3,5,7,11,.... 로 나타낼 수 있다.

참고로 500,000번째 소수는 7,368,787이다.

n번째 소수를 구하는 프로그램을 작성하시오.
'''
a=input()
a=int(a)
def prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:          
            for j in range(i+i, n, i): 
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

prime_list(7368788)[a-1]


# In[ ]:




