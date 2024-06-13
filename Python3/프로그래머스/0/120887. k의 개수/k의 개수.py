def solution(i, j, k):
    count = 0
    str_k = str(k)
    for num in range(i, j + 1):
        count += str(num).count(str_k)
    return count
