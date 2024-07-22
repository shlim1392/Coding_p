def solution(count, divisors):
    divisors.sort()
    
    s = divisors[0]
    l = divisors[-1]
    
    N = s * l
    
    return N

count = int(input())
divisors = list(map(int, input().split()))

print(solution(count, divisors))
