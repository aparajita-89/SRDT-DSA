steps = input("Enter steps: ")

level = 0
valleys = 0

for s in steps:
    if s == 'U':
        level += 1
    else:
        level -= 1

    if level == 0 and s == 'U':
        valleys += 1

print(valleys)