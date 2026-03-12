first = input("Enter first string: ")
second = input("Enter second string: ")

if sorted(first) == sorted(second):
    print(True)
else:
    print(False)