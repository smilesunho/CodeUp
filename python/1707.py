#!/usr/bin/env python
# coding: utf-8

# In[80]:
'''
10명의 프로그래밍 점수를 입력받은 후, 점수의 평균을 구하여 평균보다 높은 사람과 낮은 사람이 각각 몇 명인지 구하는 프로그램을 작성하시오.
(평균과 같은 사람은 평균보다 높은 사람에 포함시킨다.)

'''

a=input().strip().split(" ")
f=[]
for i in range(0,len(a)):
    k=float(a[i])
    f.append(k)
k=sum(f)
print('{:.1f}'.format(int(k)/len(a)))
y=k/len(a)

b=[]
c=[]
for i in range(0,len(a)):
    if float(a[i])>=y:
        b.append(a[i])
    else:
        c.append(a[i])
print(len(b), len(c))


# In[ ]:




