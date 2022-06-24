#!/usr/bin/env python
# coding: utf-8

# In[8]:


'''
두 정수 a, b를 공백으로 분리하여 입력한다.

다음 형식으로 출력한다. c, d, e, f, g에 해당되는 수는 실제 계산 결과를 의미한다.

a + b = c
a – b = d
a * b = e
a / b = f
a % b = g

'''
a,b=input().strip().split(" ")
a=int(a)
b=int(b)

c=a+b
d=a-b
e=a*b
f=a//b
g=a%b

print(a,"+",b,"=",c)
print(a,"-",b,"=",d)
print(a,"*",b,"=",e)
print(a,"/",b,"=",f)
print(a,"%",b,"=",g)

