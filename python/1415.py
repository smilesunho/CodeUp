#!/usr/bin/env python
# coding: utf-8

# In[25]:
'''
10개의 자연수를 차례대로 입력한다. (단, 10개의 자연수는 모두 1000 이하이다.)
가장 큰 홀수 하나와 짝수 하나를 출력한다. 단 홀수 혹은 짝수만 존재할 경우에는 가장 큰 수를 출력한다.
'''

a=input().strip().split(" ")
b=[]
c=[]
for i in range(0,len(a)):
    if int(a[i])%2==0:
        b.append(int(a[i]))
    else :
        c.append(int(a[i]))

b=sorted(b)
c=sorted(c)
        
if len(b)==0:
    print(max(c))
elif len(c)==0:
    print(max(b))
else:
    print(max(c), max(b))

