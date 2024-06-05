def solution(n):
    for bag in range(n // 5, -1, -1):
        remainder = n - bag * 5
        if remainder % 3 == 0:
            return bag + remainder // 3
    return -1

n = int(input())
print(solution(n))
