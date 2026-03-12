strng = input("Enter string: ")

seen = set()
left = 0
max_len = 0
for right in range(len(strng)):
    while strng[right] in seen:
        seen.remove(strng[left])
        left += 1
    seen.add(strng[right])
    max_len = max(max_len, right-left+1)
print(max_len)