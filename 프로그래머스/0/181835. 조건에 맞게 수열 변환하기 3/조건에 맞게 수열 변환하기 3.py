def solution(arr, k):
    check = k % 2 == 0
    
    for i in range(len(arr)):
        if check:
            arr[i] += k
        else:
            arr[i] *= k
    return arr