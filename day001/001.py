start = 2000
stop = 3200
nums = range(start, stop + 1)

nums_out = []
for num in nums:
    if num % 7 == 0:
        if num % 5 != 0:
            nums_out.append(num)

print(', '.join([str(n) for n in nums_out]))
