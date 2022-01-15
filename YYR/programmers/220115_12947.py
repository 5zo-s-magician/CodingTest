#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(x):
    answer = True
    dig = 0
    #a = []
    print(str(x))
    
    for i in str(x):
        #print(i)
        dig += int(i)
    # 자리수를 간단하게 구하는 방법
    # 1. str(x)를 사용하여 문자열화 -> for문을 통해 문자열의 한글자씩.. 나중에 a.append(i)를 이용해 리스트에 저장도 가능
    # 2. 제일 만만한 10으로 나눠서 1의자리부터 구하기 이때 //연산자를 사용하면 쉽게 자리수를 구한후 남은 숫자만 구할 수 있음 그리고 while(x != 0)
    # 3. map 함수를 이용하는 방법
    # map(func,iterable,...) 함수는 list 나 dic 같은 iterable 한 데이터를 인자로 받아 그 안의 개별 item을 함수의 인자로 전달하고 결과를 list의 형태로 반환해주는 함수이다
    # map 함수를 이용했을 경우 map(int, str(number))하면 문자열화 된 number의 앞자리부터 다시 int화 시킨 값을 list에 저장해서 줌
    
    if x%dig == 0:
        answer = True
    else: 
        answer = False
        
    return answer

