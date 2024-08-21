import math

def solution():
    k, a, b = map(int, input().split())

    if a % k == 0:
        start = a
    else:
        start = ((a // k) + 1) * k

    if b % k == 0:
        end = b
    else:
        end = (b // k) * k

    if start > b or end < a:
        print(0)
    else:
        count = (end - start) // k + 1
        print(count)

solution()
