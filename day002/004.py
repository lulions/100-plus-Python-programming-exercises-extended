nums = input("Insert a comma-separated list of numbers: ")
nums = nums.replace(' ', '').split(',')
nums = [int(n) for n in nums]
print(nums)
print(tuple(nums))