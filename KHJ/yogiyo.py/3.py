# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, C):
    az = [[] for i in range(26)]
    cut_list = []
    # a = 0, z = 25
    for idx, x in enumerate(S):
        az[ord(x)-ord("a")].append(idx+1)

    for l in az:
      for x in range(len(l)-1):
        tmp = [i for i in range(l[x], l[x+1])]
        cut_list.append(tmp)

    ptr = 0
    while len(cut_list) != 0:
      popp = []
      if ptr >= len(C):
        break
      x = C[ptr]
      for idx, l in enumerate(cut_list):
        if x in l:
          flag = 1
          popp.append(idx)
      if flag == 1:
        tmp = 0
        for p in popp:
          cut_list.pop(p-tmp)
          tmp += 1
      ptr += 1
    
    if len(cut_list) == 0:
      return ptr
    else:
      return -1
