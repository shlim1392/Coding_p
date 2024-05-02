def solution(n):
    a="수"
    b="박"
    c=""
    for x in range(n):
        if x % 2 == 0 :
            c += a
        else:
            c +=b
    return c