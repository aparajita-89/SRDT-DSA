num = int(input())
items = []

for i in range(num):
    name, price, discount = input().split(',')
    price = int(price)
    discount = int(discount)

    disc_amount = price * discount / 100
    items.append((name, disc_amount))

item = min(items, key=lambda x: x[1])
print(item[0])