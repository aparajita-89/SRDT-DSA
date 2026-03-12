nums = [3,0,1]

n = len(nums)
expected = n*(n+1)//2

print(expected - sum(nums))