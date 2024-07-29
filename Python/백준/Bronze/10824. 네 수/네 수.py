def solution(a,b,c,d):
    comb1 = a + b
    comb2 = c + d
    res = int(comb1) + int(comb2)
    print(res)
    
a, b, c, d = map(str, input().split())
solution(a, b, c, d)