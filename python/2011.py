#!/usr/bin/env python
# coding: utf-8

# In[15]:


'''
시작 수(a)와 마지막 수(b)가 입력되면 그 범위의 369게임의 올바른 답을 출력하시오.
※ 369게임의 룰은 다음과 같다.
1. 시작수와 마지막수까지의 369게임의 올바른 답을 출력한다.
2. 한 줄에 하나의 결과를 출력한다.
3. 369에 해당될 경우 3이나 6이나 9가 들어간 개수만큼  "K"를 출력한다.
4. 그 외의 숫자들은 그냥 그대로 출력한다.

'''
a,b=map(int,input().strip().split(" "))
k=[]
for i in range(a,b+1):
    v=str(i)
    t=0
    for j in range(0,len(v)):
        if v[j]=='3':
            t=t+1
        elif v[j]=='6':
            t=t+1            
        elif v[j]=='9':
            t=t+1
        else:
            pass
    if t!=0:
        print("K"*t)
    else:
        print(v)


        


