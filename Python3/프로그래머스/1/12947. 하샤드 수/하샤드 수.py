def solution(x):
    res = sum(int(num) for num in str(x))
    return x % res ==0