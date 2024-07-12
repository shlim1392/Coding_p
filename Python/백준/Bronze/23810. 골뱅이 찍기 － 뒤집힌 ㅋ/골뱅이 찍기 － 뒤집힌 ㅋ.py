def solution(n):
    a = "@" * 5
    for i in range(n):
        print(a*n)
    for i in range(n):
        print("@" * n)
    for i in range(n):
        print(a*n)
    for i in range(n):
        print("@" * n)
    for i in range(n):
        print("@" * n)

n = int(input())
solution(n)