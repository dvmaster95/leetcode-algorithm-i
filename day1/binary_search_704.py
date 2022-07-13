# use python 2.7 not python3

nums = [3,4,5,6,7,8]
target = 6

def bs(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot
        elif target > nums[pivot]:
            left = pivot + 1
        elif target < nums[pivot]:
            right = pivot + 1
    return -1

answer = bs(nums=nums, target=target)
print(answer)