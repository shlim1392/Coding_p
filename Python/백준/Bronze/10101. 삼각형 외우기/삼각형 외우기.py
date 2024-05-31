def triangle_type(a, b, c):
    if a + b + c != 180:
        return 'Error'
    elif a == b == c:
        return 'Equilateral'
    elif a == b or a == c or b == c:
        return 'Isosceles'
    else:
        return 'Scalene'

a = int(input())
b = int(input())
c = int(input())

print(triangle_type(a, b, c))
