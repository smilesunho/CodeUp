#!/usr/bin/env python
# coding: utf-8

# In[ ]:
'''

일차 방정식의 ax±b=0의 식을 입력받는다.

x의 값을 소숫점 둘째자리까지 출력하시오.
'''

a,b=input().split("x")
a=int(a)
b=int(b)
b=b*(-1)
k=b/a
print('{0:0.2f}'.format(k))


# In[ ]:




