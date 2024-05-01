def solution(numbers):
    res = [x for x in range(10) if x not in numbers ]
    return sum(res)