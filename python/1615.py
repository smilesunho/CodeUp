#!/usr/bin/env python
# coding: utf-8

# In[68]:
'''
어떤 자연수 n이 있을 때, d(n)을 n의 각 자릿수 숫자들과 n 자신을 더한 숫자라고 정의하자.
예를 들어 d(91) = 9 + 1 + 91 = 101 이 때, n을 d(n)의 제네레이터(generator)라고 한다.
위의 예에서 91은 101의 제네레이터이다.
어떤 숫자들은 하나 이상의 제네레이터를 가지고 있는데, 101의 제네레이터는 91 뿐 아니라 100도 있다.
그런데 반대로, 제네레이터가 없는 숫자들도 있으며, 이런 숫자를 인도의 수학자 Kaprekar가 셀프 넘버(self-number)라 이름 붙였다.
예를 들어 1,3,5,7,9,20,31 은 셀프 넘버 들이다. 
시작 값(a)과 마지막 값(b)가 입력되면 두 수 사이의 셀프 넘버들의 합을 출력하시오.

'''

a,b=input().split(" ")
a=int(a)
b=int(b)
c=[]
j=[]
if a==1 and b==1:
    print(1)
else:     
    for i in range(a,b+1):
        c.append(i)

    for k in range(0,b+1):

        if k>=1000:
            count=str (k)
            count[0:] 
            a0=int(count[0])
            a1=int(count[1])
            a2=int(count[2])
            a3=int(count[3])
            d=k+a0+a1+a2+a3
            j.append(d)
        elif k>=100:
            count=str (k)
            count[0:] 
            a0=int(count[0])
            a1=int(count[1])
            a2=int(count[2])
            d=k+a0+a1+a2
            j.append(d)
        elif k>=10:
            count=str (k)
            count[0:] 
            a0=int(count[0])
            a1=int(count[1])
            d=k+a0+a1
            j.append(d)
        else:
            count=str (k)
            count[0:] 
            a0=int(count[0])
            d=k+a0
            j.append(d)

    e=list(set(c)-set(j))
    print(sum(e))


    


# In[ ]:





# In[ ]:




