def solution(array, commands):
    answer = []
    
    for i, j, k in commands:
        arrList = array[i - 1:j]
        arrList.sort()
        
        answer.append(arrList[k - 1])
        
    return answer