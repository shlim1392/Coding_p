def solution(numbers, n):
    res = 0
    for x in numbers:
        res += x
        if res > n:
            break
    return res

# next를 활용한 코딩
def accumulate_until_exceed(numbers, n):
    return next(total for total in (sum(numbers[:i+1]) for i in range(len(numbers))) if total > n)
