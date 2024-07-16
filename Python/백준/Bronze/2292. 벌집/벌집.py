def solution(n):
    if n == 1:
        return 1
    layer = 1
    range_end = 1
    while range_end < n:
        range_end += 6 * layer
        layer += 1
    return layer

n = int(input())
print(solution(n))
