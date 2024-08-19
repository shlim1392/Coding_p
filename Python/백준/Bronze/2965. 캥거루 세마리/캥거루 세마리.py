def solution():
    A, B, C = map(int, input().split())
    gap1 = B - A
    gap2 = C - B
    print(max(gap1, gap2) - 1)

solution()