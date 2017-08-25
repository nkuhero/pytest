def two_num(nums, target):
    hash = {}
    for i in range(len(nums)):
        if target - nums[i] in hash: 
            return [hash[target - nums[i]], i]
        else:
            hash[nums[i]] = i

    return [-1, -1]

nums = [2, 7, 11, 15]
target = 18

print(two_num(nums, target))
