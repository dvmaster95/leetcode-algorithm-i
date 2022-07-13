nums = [0]
inters = [x for x in nums if x != 0]
zeros = [x for x in nums if x == 0]
nums[:] = inters + zeros
print(nums)