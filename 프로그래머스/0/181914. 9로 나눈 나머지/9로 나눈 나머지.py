def solution(number):
    
    numberl = map(int, number)
    answer = (sum(numberl) % 9)
    return answer