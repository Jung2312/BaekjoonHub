def solution(numLog):
    dic = {1 : 'w', -1 : 's', 10 : 'd', -10 : 'a'}
    answer = []
    
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i-1]
        if diff in dic:
            answer.append(dic.get(diff))
        
    return ''.join(answer)