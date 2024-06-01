def solution(a, b, c):
    sides = sorted([a, b, c])
    if sides[0] + sides[1] > sides[2]:
        return sum(sides)
    else:
        return 2 * (sides[0] + sides[1]) - 1

a, b, c = map(int, input().split())
print(solution(a, b, c))
