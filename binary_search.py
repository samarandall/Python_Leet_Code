nums = [-1,0,3,5,9,12]
target = 9

nums_right = len(nums)-1
nums_left = 0
bool = True
while nums_left < nums_right:
    midpoint = (nums_right + nums_left)//2
    if nums[midpoint] == target:
        print(midpoint)
        bool = False
        break
    elif nums[midpoint] < target:
        nums_left = midpoint + 1
    else:
        nums_right = midpoint - 1

if bool: print("-1")