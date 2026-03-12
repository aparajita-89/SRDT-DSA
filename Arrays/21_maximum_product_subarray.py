nums = [2,3,-2,4]

max_prod = nums[0]
min_prod = nums[0]
result = nums[0]

for i in nums[1:]:
    temp = max(i, max_prod*i, min_prod*i)
    min_prod = min(i, max_prod*i, min_prod*i)
    max_prod = temp
    result = max(result, max_prod)

print(result)