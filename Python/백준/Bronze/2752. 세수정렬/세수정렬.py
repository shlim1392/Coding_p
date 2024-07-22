def solution(a, b, c):
    res = [a, b, c]
    res.sort()  
    print(" ".join(map(str, res)))  

a, b, c = map(int, input().split())
solution(a, b, c)
