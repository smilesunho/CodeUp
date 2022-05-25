#!/usr/bin/env python
# coding: utf-8

# In[36]:
'''
1, 2, 3 ... 을 계속 더해 나갈 때,
그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
계속 더하는 프로그램을 작성해보자.


'''

a=input()
a=int(a)
b=int (0)
c=int (0)
while True:
    if c>=a:
        b=b-1
        print(b)
        break
    else :
        c=c+b
        b=b+1
    


# In[ ]:





# In[ ]:




