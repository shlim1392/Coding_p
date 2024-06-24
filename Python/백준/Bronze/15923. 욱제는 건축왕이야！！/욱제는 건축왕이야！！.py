def solution(coordinates):
    n = len(coordinates)
    perimeter = 0
    
    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]
        perimeter += abs(x1 - x2) + abs(y1 - y2)  
    return perimeter


N = int(input())
coordinates = []
for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

result = solution(coordinates)
print(result)
