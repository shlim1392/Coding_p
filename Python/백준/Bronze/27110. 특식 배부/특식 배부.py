def solution(a, b, c, n):
    fried_satisfied = min(n, a)
    soy_satisfied = min(n, b)
    spicy_satisfied = min(n, c)
    
    max_satisfied = fried_satisfied + soy_satisfied + spicy_satisfied
    return max_satisfied

n=int(input())
a, b, c = map(int, input().split())
print(solution(a, b, c, n))
