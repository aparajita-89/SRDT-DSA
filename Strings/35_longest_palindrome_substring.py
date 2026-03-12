strng = input("Enter string: ")

longest = ""

for i in range(len(strng)):
    for j in range(i, len(strng)):
        sub = strng[i:j+1]

        if sub == sub[::-1] and len(sub) > len(longest):
            longest = sub

print(longest)