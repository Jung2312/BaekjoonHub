def solution(a, d, included):
    answer = 0
    aList = [a]

    for i in range(len(included)):
        if included[i]:
            aList.append(aList[i] + d)
            answer += aList[i]
        else:
            aList.append(aList[i] + d)  
        
    
    return answer