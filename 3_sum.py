nums = [-1,0,1,2,-1,-4]

def threeSum(nums):
    if len(nums) < 3:
        return []
    nums.sort()


    tripples = list()
    
    for i in range(0,len(nums)-2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                tripples.append(tuple(sorted([nums[i], nums[left], nums[right]])))
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
        
    return list(set(tripples))
        

print(threeSum(nums))