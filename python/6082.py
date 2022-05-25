#!/usr/bin/env python
# coding: utf-8

# In[30]:
'''

1 부터 그 수까지 순서대로 공백을 두고 수를 출력하는데,
3 또는 6 또는 9가 포함 되어있는 수인 경우, 그 수 대신 영문 대문자 X 를 출력한다.


'''


a=input()
a=int(a)
b=[]
c=[]
for i in range (1,a+1):
    b.append(i)
while True:
    for k in range(0,a):
        if b[k]==3 or b[k]==6 or b[k]==9:
            c.append('X')
        elif b[k]%10==3 or b[k]%10==6 or b[k]%10==9: 
            c.append('X')
        else :
            c.append(b[k])
        print (c[k], end=' ')
    break


# In[ ]:




