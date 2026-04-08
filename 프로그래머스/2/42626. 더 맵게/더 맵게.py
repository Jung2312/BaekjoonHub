import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        scov1 = heapq.heappop(scoville) 
        scov2 = heapq.heappop(scoville) 
        heapq.heappush(scoville, scov1 + (scov2 * 2))
        answer += 1

    return answer