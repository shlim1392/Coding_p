def solution(my_string):
    res = 0
    for x in my_string:
        if x.isdigit():
            res += int(x)
    return res