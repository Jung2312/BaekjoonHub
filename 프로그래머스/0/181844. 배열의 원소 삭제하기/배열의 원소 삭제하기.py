def solution(arr, delete_list):
    for i in delete_list:
        arr = [x for x in arr if x != i]

    return arr