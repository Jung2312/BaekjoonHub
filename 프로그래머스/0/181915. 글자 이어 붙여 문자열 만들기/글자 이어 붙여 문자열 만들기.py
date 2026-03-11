def solution(my_string, index_list):
    strList = list(my_string)
    answer = ""
    
    for a in index_list:
        answer += strList[int(a)]
    
    return answer