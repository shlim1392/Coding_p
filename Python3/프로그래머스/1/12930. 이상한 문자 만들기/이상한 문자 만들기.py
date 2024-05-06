def solution(s):
    res = ''
    index = 0
    for x in s:
        if x == ' ':
            res += x
            index = 0
        else:
            if index % 2 == 0:
                res += x.upper()
            else:
                res += x.lower()
            index += 1
    return res