def solution(nums):
    setnum = set(nums)
    answer = 0 
    num = len(nums) / 2
    
    if len(setnum) - num > 0:
        answer = len(setnum) - (len(setnum) - num)
    else:
        answer = len(setnum)
        
    return answer