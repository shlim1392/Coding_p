def max_n(S):
    n = 1
    sum_n = 0
    while True:
        sum_n += n
        if sum_n > S:
            return n - 1
        n += 1

S = int(input())
print(max_n(S))
