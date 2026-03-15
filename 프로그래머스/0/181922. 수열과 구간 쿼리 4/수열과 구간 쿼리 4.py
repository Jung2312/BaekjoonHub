def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e + 1):
            if k == 0:
                if i == 0:
                    arr[i] += 1
            else:
                if i % k == 0:
                    arr[i] += 1
    return arr