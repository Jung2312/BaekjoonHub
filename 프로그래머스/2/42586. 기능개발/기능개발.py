import math
def solution(progresses, speeds):
    answer = []
    temp = []
    
    for a, b in zip(progresses, speeds):
        ceil = math.ceil((100 - a) / b)
        temp.append(ceil)
        
    standard = temp[0]
    cnt = 1
    
    for i in range(1, len(temp)):
        if temp[i] <= standard:
            cnt += 1
        else:
            standard = temp[i]
            answer.append(cnt)
            cnt = 1
            
    answer.append(cnt)

    return answer