arr = [1,2,4,7,7,5]

arr = sorted(set(arr))

if len(arr) < 2:
    print(-1,-1)
else:
    print("Second Smallest:", arr[1])
    print("Second Largest:", arr[-2])