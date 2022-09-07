nums = [2,7,11,15]
target = 9

hash_map = {target-nums[0]: 0}

for i in range(1, len(nums)):
    if nums[i] in hash_map:
        print([hash_map[nums[i]], i])
    hash_map[target-nums[i]] = i
