import math

def solution(num_list):
    answer = 1 if sum(num_list) ** 2 > math.prod(num_list) else 0
    return answer