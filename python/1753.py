#!/usr/bin/env python
# coding: utf-8

# In[27]:


'''
어떤 회사에서는 이름을 사용하지 않고 코드네임이라는 것을 사용한다.
이때 코드네임을 만드는 방법이 있는데 자신의 성을 제외한 이름만 영어로 바꾸어서 뒤집어 읽는것이라고 한다.
이 때 n명의 사람의 영어 이름이 입력될 때 n명의 코드네임을 출력하시오.

첫째줄에 n명이 입력된다.  (1<=n<=100)
2번째줄부터 n명의 영어이름이 입력된다.(영어이름은 알파벳 소문자만 입력되고, 최대길이 100글자이내)
'''
a=input()
a=int(a)
i=0
z=[]
while i<a:
    k=input()
    z.append(k)
    i=i+1

for i in range(0,len(z)):
    k=z[i]
    k=str (k)
    k=list(k)
    k.reverse()
    k=''.join(k)
    print(k)
    


# In[ ]:




