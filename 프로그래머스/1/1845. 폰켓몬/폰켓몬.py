def solution(nums):
    numsdiv = len(nums) / 2
    setnums = set(nums)
 
    return len(setnums) if len(setnums) < numsdiv else numsdiv