#!/usr/bin/env python
# coding: utf-8

# In[ ]:
'''
등차 수열은 일정한 값을 더해서 다음 항이 결정되는 수열을 말한다.
등차수열의 예)
1, 3, 5, 7, 9 ....  첫항이 1이고, 공차(=두 수 사이의 간격)가 2인 등차수열
4, 9, 14, 19, 24, ... 첫 항이 4이고, 공차가 5인 등차수열
입력으로 첫항, 둘째항, k값이 주어졌을 때, 이 등차수열의 첫번째 항부터 k값 이하의 항까지 출력하시오
'''

a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
d=b-a
for i in range (0,c):
    if a+d*i<=c:
        print(a+d*i, end=' ')
    else :
        break





# In[ ]:




