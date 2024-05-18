def solution(arr):
    n = len(arr)
    power = 0
    while 2 ** power < n:
        power += 1
    zero_count = (2 ** power) - n
    arr.extend([0] * zero_count)
    return arr



