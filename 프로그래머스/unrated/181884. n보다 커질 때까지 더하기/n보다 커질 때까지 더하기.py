def solution(numbers, n):
    res = 0
    for x in numbers:
        res += x
        if res > n:
            break
    return res

