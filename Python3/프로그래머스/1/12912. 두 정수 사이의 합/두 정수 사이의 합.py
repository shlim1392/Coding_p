def solution(a, b):
    res = []
    if a < b:
        for x in range(a, b+1):
            res.append(x)
    else:
        for x in range(b, a+1):
            res.append(x)      
    return sum(res)