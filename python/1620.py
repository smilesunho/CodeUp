#!/usr/bin/env python
# coding: utf-8

# In[113]:
'''
어떤 수 n이 입력되면 n의 각 자릿수의 합이 한 자리가 될때까지 계산하여 출력하시오.
예) 1234567
1234567 → 1+2+3+4+5+6+7 = 28 → 2 + 8 = 10 → 1 + 0 = 1

'''


a=list(str(input()))
k=len(a)
b=[]
for i in range(0,k):
    j=int(a[i])
    b.append(j)
if sum(b)<10:
    print(sum(b))
else:
    t=sum(b)
    while True:
        t=str(t)
        y=len(t)
        k=[]
        for i in range(0,y):
            b=list(str(t))
            j=[]
            j=int(b[i])
            k.append(j)
        if sum(k)<10:
            print(sum(k))
            break
        else:
            t=sum(k)

        
    


# In[ ]:





# In[ ]:




