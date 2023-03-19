N = input().rstrip()

NL = [x for x in N]

for i in range(len(NL)):
    max = i
    for j in range(i+1, len(NL)):
        if NL[j] > NL[max]:
            max = j
    
    NL[i], NL[max] = NL[max], NL[i]

print("".join(NL))