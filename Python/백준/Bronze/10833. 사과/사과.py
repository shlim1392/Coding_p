def solution(n):
    total = 0
    for _ in range(n):
        a, b = map(int, input().split())
        ex = b % a
        total += ex
    print(total)
    
n = int(input())
solution(n)
        
        