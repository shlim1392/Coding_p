def solution(t, p):
    res = 0
    p_len = len(p)
    p_num = int(p)
    for i in range(len(t) - p_len + 1):
        sub_str = t[i:i+p_len]
        sub_num = int(sub_str)
        if sub_num <= p_num:
            res += 1
            
    return res