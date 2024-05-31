n = int(input())
x = []
y = []

def solution(x, y):
    width = max(x) - min(x)
    height = max(y) - min(y)
    return width * height

for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    
if n == 1:
    print(0)
else:
    area = solution(x, y)
    print(area)
    