strng = input("Enter string: ")
goal = input("Enter goal: ")

if goal in (strng + strng):
    print(True)
else:
    print(False)