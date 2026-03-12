num = int(input())

if num == 0:
    print("No Factors")
else:
    num = abs(num)
    for i in range(1, num+1):
        if num % i == 0:
            print(i, end=" ")