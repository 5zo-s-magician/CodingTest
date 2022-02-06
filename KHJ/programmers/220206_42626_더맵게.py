import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        first = heapq.heappop(scoville)
        if first >= K:
            return answer
        if len(scoville) == 0 and first<K:
            return -1
        second = heapq.heappop(scoville)
        new = first + second*2
        heapq.heappush(scoville,new)
        answer += 1
    return answer


#난 직접구현했는데... 모듈이 이미 있구나.. 당연하긴하지....
# def make_heap(arr):
#     arr = [-1]+arr
#     for i in range((len(arr)-1)//2,0,-1):
#         arr = min_heapify(arr,i)
#     return arr[1:]
    
# def min_heapify(heap,i):
#     while len(heap)-1 >= 2*i:
#         if len(heap)-1 == 2*i:
#             child = 2*i
#         else:
#             child = 2*i if heap[2*i]<=heap[2*i+1] else 2*i+1
        
#         if heap[i]>heap[child]:
#             heap[i] , heap[child] = heap[child], heap[i]
#             i = child
#         else:
#             return heap
#     return heap

# def insert(heap,key):
#     heap = [-1]+heap+[key]
#     i = len(heap) -1
#     while i>1 and heap[i//2] > heap[i]:
#         heap[i//2], heap[i] = heap[i], heap[i//2]
#     return heap[1:]
    
    
# def extract_min(heap):
#     extract = heap[0]
#     heap[0] = heap[-1]
#     heap = [-1] + heap[:-1]
#     heap = min_heapify(heap,1)
#     return heap[1:], extract