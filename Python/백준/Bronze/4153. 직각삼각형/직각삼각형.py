def is_right_triangle(sides):
    sides.sort()
    a, b, c = sides
    return a**2 + b**2 == c**2

while True:
    sides = list(map(int, input().split()))
    if sides == [0, 0, 0]:
        break
    if is_right_triangle(sides):
        print("right")
    else:
        print("wrong")

    