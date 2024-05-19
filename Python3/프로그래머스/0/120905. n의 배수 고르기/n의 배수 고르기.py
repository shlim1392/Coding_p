def solution(n, numlist):
    res = []
    for x in numlist:
        if x % n == 0:
            res.append(x)
    return res