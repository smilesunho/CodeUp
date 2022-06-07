#!/usr/bin/env python
# coding: utf-8

# In[22]:


'''
20글자 이하의 한 단어가 입력되면 뒤집어 출력하시오.
예) love → evol
'''
a=input()
a=str(a)
a=list(a)
a.reverse()
a=''.join(a)
print(a)


# In[ ]:




