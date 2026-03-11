def solution(n, control):
    dicList = {"w": 1, "s": -1, "d": 10, "a": -10}
    list = control[0:]
        
    for l in list:
        n += dicList[l]
            
    return n