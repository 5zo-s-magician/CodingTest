#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(x, n):
    answer = []
    temp = x
    answer.append(x)
    for i in range(n-1):
        temp += x
        answer.append(temp)
    
    
    return answer

