nums = [3,2,3]

def majorityElement(nums):
    size_of_nums = len(nums)
    majority_size = size_of_nums//2
    count_of_nums_dict = {}
    for number in nums:
        if count_of_nums_dict.get(number):
            count_of_nums_dict[number] += 1
        else:
            count_of_nums_dict[number] = 1
        if count_of_nums_dict[number] > majority_size:
            return number

print(majorityElement(nums))

