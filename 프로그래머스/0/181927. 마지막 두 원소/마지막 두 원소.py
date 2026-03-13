def solution(num_list):
    answer = []
    
    end = num_list[len(num_list) - 1]
    beforeEnd = num_list[len(num_list) - 2]
    
    num_list.append(end - beforeEnd) if end > beforeEnd else num_list.append(end * 2)
    
    return num_list