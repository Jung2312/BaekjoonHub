def solution(a, b):
    list = [int(str(a) + str(b)), int(str(b) + str(a))]
    
    return int(f"{max(list)}")