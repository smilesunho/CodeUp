#!/usr/bin/env python
# coding: utf-8

# In[19]:
'''
아이유는 다음과 같은 날을 "좋은 날"이라고 정했다.^^
- 연도와 월,일이 입력되면, (연도 4자리)와 (월,일을 합친 4자리 숫자)가 같은 숫자 구성으로 된 날을 말한다. 
예를 들어, 2012년 12월 02일은 좋은 날이다.
연도인 2012와 월일을 합친 1202의 숫자 구성이 같기 때문이다.
"좋은 날"을 판별하는 프로그램을 작성하시오.
'''

a,b,c=input().split("/")
a=list(a)
b=list(b)
c=list(c)
d=b+c
a=sorted(a)
d=sorted(d)
if a==d:
    print("yes")
else :
    print("no")


# In[ ]:




