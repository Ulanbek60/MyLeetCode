def majorityElementnums(nums):
    result = 0
    for i in nums:
            result ^= i
    return result

print(majorityElementnums([3,2,3]))


