strng = input("Enter string: ")

for ch in strng:
    if strng.count(ch) == 1:
        print(ch)
        break