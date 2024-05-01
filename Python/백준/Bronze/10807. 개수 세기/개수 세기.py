n = int(input())
b = list(map(int, input().split(" ")))
v = int(input())

def solution(b, v):
    res = 0
    for s in b : 
        if s == v:
            res += 1
    return res

print(solution(b, v))