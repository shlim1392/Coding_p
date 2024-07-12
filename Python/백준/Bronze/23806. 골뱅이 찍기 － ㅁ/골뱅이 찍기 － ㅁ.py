def solution(n):
    a = "@" * 5
    b = "@"
    c = "   "
    for i in range(n):
        print(a*n)
    for i in range(n):
        print((b*n) + (c*n) + (b*n))
    for i in range(n):
        print((b*n) + (c*n) + (b*n))
    for i in range(n):
        print((b*n) + (c*n) + (b*n))
    for i in range(n):
        print(a*n)
        
n = int(input())
solution(n)
