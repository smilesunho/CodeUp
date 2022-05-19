#!/usr/bin/env python
# coding: utf-8

# In[ ]:
#"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

y, m, d = input().split('.')
print(d,m,y,sep='-')

