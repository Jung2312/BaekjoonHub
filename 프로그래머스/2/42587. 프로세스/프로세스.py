def solution(priorities, location):
    q = [(p, i) for i, p in enumerate(priorities)]
    answer = 0
    
    while q:
        cur = q.pop(0)
        
        if any(cur[0] < x[0] for x in q):
            q.append(cur)
        else:
            answer += 1
            if cur[1] == location:
                return answer