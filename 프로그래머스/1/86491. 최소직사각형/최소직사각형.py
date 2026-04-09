def solution(sizes):
    sizes = [sorted(x, reverse=True) for x in sizes]
    
    frontList = []
    backList = []
    
    for i, j in sizes:
        frontList.append(i)
        backList.append(j)
        
    
    return max(frontList) * max(backList)