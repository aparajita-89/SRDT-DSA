strng = input("Enter string: ")

result = ""
count = 1

for i in range(1,len(strng)):
    if strng[i] == strng[i-1]:
        count += 1
    else:
        result += strng[i-1] + str(count)
        count = 1

result += strng[-1] + str(count)

print(result)