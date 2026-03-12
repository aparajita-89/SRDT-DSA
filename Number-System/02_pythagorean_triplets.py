num = int(input("limit: "))

for a in range(1, num):
    for b in range(a+1, num):
        for c in range(b+1, num):
            if a*a + b*b == c*c:
                print(a, b, c)