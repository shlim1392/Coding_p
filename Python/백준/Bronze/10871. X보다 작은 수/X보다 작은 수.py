n, x = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

def solution(x, a):
    res = []
    for c in a:
        if c < x:
            res.append(c)
    return ' '.join(map(str, res))

print(solution(x, a))