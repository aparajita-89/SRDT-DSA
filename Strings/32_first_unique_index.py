strng = input("Enter string: ")

for i in range(len(strng)):
    if strng.count(strng[i]) == 1:
        print(i)
        break
else:
    print(-1)