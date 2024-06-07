def solution(a, b, v):
    if a >= v:
        return 1
    days_needed = (v - b - 1) // (a - b) + 1
    return days_needed

a, b, v = map(int, input().split())
print(solution(a, b, v))