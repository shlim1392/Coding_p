def solution():
    n = int(input())
    num = []
    for _ in range(n):
        a = list(map(int, input().split()))
        num.append(a)
    
    sort_point = sorted(num, key=lambda point: (point[0], point[1]))
    
    for point in sort_point:
        print(point[0], point[1])

solution()
