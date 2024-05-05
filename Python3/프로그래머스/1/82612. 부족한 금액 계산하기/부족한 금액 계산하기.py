def solution(price, money, count):
    s = sum(price * n for n in range(1, count + 1))
    res = s - money
    return 0 if res <= 0 else res