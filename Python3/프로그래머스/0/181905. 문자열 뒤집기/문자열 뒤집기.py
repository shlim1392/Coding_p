def solution(my_string, s, e):
    res = list(my_string)
    res[s:e+1] = my_string[s:e+1][::-1]
    return ''.join(res)