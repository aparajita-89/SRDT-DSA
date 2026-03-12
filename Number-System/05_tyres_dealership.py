num = int(input())

for i in range(num):
    cars, bikes = map(int, input().split())
    tyres = cars*4 + bikes*2
    print(tyres)