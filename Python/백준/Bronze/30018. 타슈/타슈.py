def solution(a, b):
    N = len(a)
    diff = [a[i] - b[i] for i in range(N)]
    total_moves = sum(abs(d) for d in diff) // 2    
    return total_moves

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


result = solution(a, b)
print(result)
