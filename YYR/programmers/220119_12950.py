def solution(arr1, arr2):
    
    answer = [[] for x in range(len(arr1))]
    # 빈 리스트를 설정할때 []의 갯수를 주어진 행렬과 같게 하지 않으면 오류가 난다.
  
    # arr1[0][0] + arr2[0][0]
    # arr1[0][1] + arr2[0][1]...
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            answer[i].append(arr1[i][j]+arr2[i][j])
            # answer[i][j] = 어쩌구 는 오류가 남. append 를 활용해야 한다.
    
       
    return answer