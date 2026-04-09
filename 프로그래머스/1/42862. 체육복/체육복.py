def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve) #잃어버린 사람 중에 여분 가진 사람 제거
    reserve_set = set(reserve) - set(lost) #잃어버린 사람 중에 여분 가진 사람 제거
    
    for i in reserve_set:
        if i - 1 in lost_set:
            lost_set.remove(i-1)
        elif i + 1 in lost_set:
            lost_set.remove(i+1)
            
    return n - len(lost_set)