import re

def solution(str1, str2):
    answer = 0
    # 전처리
    # str1 = ''.join(filter(str.isalpha, str1))
    # str2 = ''.join(filter(str.isalpha, str2))
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 프로세스
    str1_list = [str1[i:i+2] for i in range(len(str1)-1)]
    str2_list = [str2[i:i+2] for i in range(len(str2)-1)]
    str1_list = [val for val in str1_list if val.isalpha()]
    str2_list = [val for val in str2_list if val.isalpha()]
    #print(str1_list, str2_list)
    
    gyo = [val for val in str1_list if val in str2_list]
    hap = [val for val in str1_list if val not in gyo]
    #print("q", hap)
    hap += [val for val in str2_list if val not in gyo]
    #print("p", hap)
    hap_count = len(hap)
    gyo_set = list(set(gyo))
    real_gyo = []
    for val in gyo_set:
        one = str1_list.count(val)
        two = str2_list.count(val)
        #print(val, one, two)
        maxx = max(one,two)
        minn = min(one, two)
        
        hap += [val for i in range(maxx)]
        real_gyo += [val for i in range(minn)]
    
    if len(hap) == 0:
        return 65536
    return (len(real_gyo)/len(hap))*65536//1