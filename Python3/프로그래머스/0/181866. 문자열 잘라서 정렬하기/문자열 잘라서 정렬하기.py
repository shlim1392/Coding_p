def solution(myString):
    parts = myString.split('x')
    res_list = [part for part in parts if part]
    res = sorted(res_list)
    return res

