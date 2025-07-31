def singleNumber(nums):
    for i in nums:
        if nums.count(i) == 1: 
            return i 
    return 'f'
 

print(singleNumber([2,2,1, 1]))
