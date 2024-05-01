def solution(arr, divisor):
    res = [x for x in arr if x % divisor == 0]
    return sorted(res) if res else [-1]
