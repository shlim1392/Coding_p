def solution(n):
    res = n//7
    if n // 7 == 0 :
        res = 1
    elif (n % 7) > 0 :
        res += 1
    return res