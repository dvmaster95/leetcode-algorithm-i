nums = [1,2,3,4,5,6,7]
k = 3

if k <= len(nums):
    nums = nums[-k:] + nums[:-k]
else:
    pass

print(nums)