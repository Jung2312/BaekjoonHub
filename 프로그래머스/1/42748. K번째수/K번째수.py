def solution(array, commands):
    answer = []
    
    for i in commands:
        num1 = i[0] - 1
        num2 = i[1]
        num3 = i[2] - 1
        
        arrList = array[num1:num2]
        arrList.sort()
        
        answer.append(arrList[num3])
        
    return answer