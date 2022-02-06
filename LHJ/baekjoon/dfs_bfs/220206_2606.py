from sys import stdin

read = stdin.readline
computer_dic={}

# 입력받은 그래프 정보를 computer_dic에 초기화
for i in range(int(read())):
    computer_dic[i+1] = set()

for j in range(int(read())):
    a, b = map(int,read().split())
    computer_dic[a].add(b)
    computer_dic[b].add(a)

# dfs탐색 함수
def dfs(start, dic):
    for i in computer_dic[start]: # 해당 컴퓨터와 이어진 컴퓨터들마다 탐색진행
        if i not in infection: # 아직 infection으로 판정시키지 않은 노드(컴퓨터)라면
            infection.append(i) # 넣고
            dfs(i, computer_dic) # 그 컴퓨터와 연결된 경로들에 대한 탐색을 진행

infection = []

start_com = 1

dfs(start_com, computer_dic)

result = len(infection) - 1 # 총 감염된 컴퓨터 수 중 첫 컴퓨터는 제외해야 하므로

print(result)