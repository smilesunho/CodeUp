#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
문제 설명    
은우와 건우는 게임을 하고 있다.
둘다 100점으로 출발한다.
게임에서 일반적인 6면의 주사위를 사용한다.
한 라운드에서 주사위 숫자를 비교해서 작은 사람이 큰 사람의 점수 만큼 점수가 빼게 된다.
이때 주사위의 숫자가 같을 경우는 점수의 변화가 없게 된다.

첫 줄에 총 게임 회수(n)가 입력된다 ( 1<=n<=15 인 정수)
다음 줄 부터 n+1줄에 걸쳐 은우와 건우의 주사위 값이 공백으로 구분해서 입력된다. 이 때 주사위의 값은 1부터 6까지이다.

출력
첫줄에 은우의 점수를 출력하고,
둘째 줄에 건우의 점수를 출력한다.
'''
a=input()
a=int(a)
b=[100]
c=[100]
for i in range(0,a):
    d,e=map(int,input().split(" "))
    if d>e:
        b.append(-d)
    elif d<e:
        c.append(-e)
    else:
        pass
print(sum(c))        
print(sum(b))
        


# In[ ]:




