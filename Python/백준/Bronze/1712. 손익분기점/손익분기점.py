def bep(A, B, C):
    if C <= B:
        return -1
    else:
        return (A // (C - B)) + 1

A, B, C = map(int, input().split())

print(bep(A, B, C))