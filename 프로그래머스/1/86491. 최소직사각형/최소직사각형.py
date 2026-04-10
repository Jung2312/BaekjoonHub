def solution(sizes):
    flist = []
    blist = []
    for arr in sizes:
        flist.append(max(arr))
        blist.append(min(arr))
    return max(flist) * max(blist)