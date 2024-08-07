import math

def count_min_transitions(x1, y1, x2, y2, planets):
    def is_inside_circle(x, y, cx, cy, r):
        return (x - cx) ** 2 + (y - cy) ** 2 < r ** 2

    count = 0
    for (cx, cy, r) in planets:
        start_inside = is_inside_circle(x1, y1, cx, cy, r)
        end_inside = is_inside_circle(x2, y2, cx, cy, r)
        if start_inside != end_inside:
            count += 1

    return count


T = int(input())
results = []
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = [tuple(map(int, input().split())) for _ in range(n)]
    result = count_min_transitions(x1, y1, x2, y2, planets)
    results.append(result)


for result in results:
    print(result)
