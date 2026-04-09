import heapq as hq 

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) < 2:
            answer = -1
            return answer
        
        num1 = hq.heappop(scoville)
        num2 = hq.heappop(scoville)
        
        hq.heappush(scoville, num1 + (num2 * 2))
        answer += 1
    
    return answer