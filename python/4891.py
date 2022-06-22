#!/usr/bin/env python
# coding: utf-8

# In[6]:


'''
가장 높은 점수와 가장 낮은 점수의 차이를 출력한다.

[입력예시]
5
27 35 92 75 42
[출력예시]
65
'''
import numpy as np
b=input()
a=list(map(int,input().strip().split(" ")))
c=np.max(a)-np.min(a)
print(c)


# In[ ]:




