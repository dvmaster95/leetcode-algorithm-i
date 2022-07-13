numbers = [-1, 0]
target = -1

hash_map = {}
for index, value in enumerate(numbers):
    diff = target - value
    if diff in hash_map:
        result = [hash_map[diff], index+1]
        break
    hash_map[value] = index + 1

print(result)
