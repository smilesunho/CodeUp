#!/usr/bin/env python
# coding: utf-8

# In[75]:
'''
1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되,
3의 배수인 경우는 출력하지 않도록 만들어보자.
'''

a=input()
a=int(a)
for i in range(1,a+1):
    if i%3 !=0:
        print(i,end=' ')
    else:
        continue



# In[ ]:




