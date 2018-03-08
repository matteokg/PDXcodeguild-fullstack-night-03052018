nums = [5, 0, 8, 3, 4, 1, 6, 3, 2, 29, 48, 59, 9000, -29]


average = 0
sum = 0
for n in nums:
    sum = sum + n
average = sum / len(nums)

print(average)
