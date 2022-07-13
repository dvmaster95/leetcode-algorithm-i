nums = [-7,-3,2,3,11]
k = 99
k = k % len(nums)
nums[:] = nums[-k:] + nums[:-k]
print(nums)
