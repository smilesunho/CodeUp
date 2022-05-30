#!/usr/bin/env python
# coding: utf-8

# In[40]:
'''
정수 N을 입력받아 1~N*N까지 2차원 배열에 저장한 후 사각 테두리에 있는 배열값들만 합하여 출력하시오.
예를 들어) 3을 입력한다면
1 2 3
4 5 6
7 8 9 와 같이 배열에 저장한 후 테두리의 값인 1+2+3+6+9+8+7+4 = 40을 출력하는 프로그램을 작성하시오.
'''
a=int(input())
k=[]
if a==1:
    print(1)
    
elif a==2:
    print(10)
else :
    b=int((a+1)*a/2)
    for i in range(1,a-1):
        k.append(a*i+1+a*(i+1))
        c=int((a*a+(a*(a-1)+1))*a/2)
    d=sum(k)
    print(b+d+c)
    
    
    


# In[ ]:





# In[ ]:




