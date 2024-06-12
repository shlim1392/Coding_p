def solution(num, k):
    num_str = str(num)
    k_str = str(k)
    pos = num_str.find(k_str)
    if pos == -1:
        return -1
    else :
        return pos +1