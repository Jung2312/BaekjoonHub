def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        temp = [x for x in arr[s:e+1] if x > k]
        answer.append(min(temp) if temp else -1)
        
    return answer