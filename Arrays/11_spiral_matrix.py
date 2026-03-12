matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

result = []

while matrix:
    result += matrix.pop(0)

    for row in matrix:
        if row:
            result.append(row.pop())

    if matrix:
        result += matrix.pop()[::-1]

    for row in matrix[::-1]:
        if row:
            result.append(row.pop(0))

print(result)