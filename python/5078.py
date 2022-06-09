#!/usr/bin/env python
# coding: utf-8

# In[9]:


'''
여러가지 삼각형의 타입이 있을 것이다.
삼각형의 세 각이 주어지면 어떤 삼각형인지 출력하는 것이다.
1. 세각이 전부 60도이면 Equilateral(정삼각형)
2. 세각의 합이 180도 이고 정확히 두 각이 같은 경우 Isosceles(이등변삼각형)
3. 세각의 합이 180도이고 두 각이 같지 않을 때는 Scalene(부등변삼각형)
4. 세각의 합이 180도 아니면 Error(오류)

세 줄에 걸쳐서 세각이 주어진다. ( 0< 각 <180)
'''
a=input()
a=int(a)
b=input()
b=int(b)
c=input()
c=int(c)
if a==60 and b==60 and c==60:
    print("Equilateral")
elif a+b+c==180:
    if (180-a)/2==b and (180-a)/2==c:
        print("Isosceles")
    elif (180-c)/2==b and (180-c)/2==a:
        print("Isosceles")
    elif (180-b)/2==c and (180-b)/2==a:
        print("Isosceles")
    else :
        print("Scalene")
else:
    print("Error")


# In[ ]:




