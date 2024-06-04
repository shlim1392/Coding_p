def solution(n):
    for i in range(1, n):
        dec_sum = i + sum(map(int, str(i)))
        if dec_sum == n:
            return i
    return 0

n = int(input())
print(solution(n))