def equation(a, b, c):
    result = (a*a*a) + (a*a*b) + (2*a*a*b) + (2*a*b*b) + (a*b*b) + (b*b*b)
    return result


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

ans = equation(a, b, c)

print("Result of the equation is:", ans)