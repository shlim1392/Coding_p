def solution(n):
    a = [x for x in range(int(n+1)) if x % 2 == 0]
    return sum(a)
