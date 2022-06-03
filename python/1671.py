#!/usr/bin/env python
# coding: utf-8

# In[4]:
'''
광현이와 컴퓨터가 가위바위보 게임을 한다. 
가위바위보 게임의 규칙이 다음과 같을때 결과를 출력하시오.
(※ 바위=0, 가위=1, 보=2를 말한다.)
1. 바위(0)는 가위(1)를 이긴다.
2. 가위(1)는 보(2)를 이긴다.
3. 보(2)는 바위(0)를 이긴다.
4. 같은 것을 내면 비긴다.
입출력의 설명을 참고하여 가위바위보 게임의 결과를 출력하시오.
결과는 광현이 중심으로 출력한다.
'''

a,b=input().split(" ")
a=int(a)
b=int(b)
if b==0:
    if a==2:
        print("win")
    elif a==1:
        print("lose")
    else:
        print("tie")
else:
    if b-a==1:
        print("win")
    elif b-a==0:
        print("tie")
    else:
        print("lose")


# In[ ]:




