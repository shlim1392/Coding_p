def solution(order):
    res = 0
    for x in str(order):
        if x == "3" or x == "6" or x == "9":
            res += 1
    return res