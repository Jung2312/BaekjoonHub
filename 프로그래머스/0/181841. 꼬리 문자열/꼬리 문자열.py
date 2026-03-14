def solution(str_list, ex):
    str_list = [ x for x in str_list if ex not in x ]
    answer = "".join(str_list)
    return answer