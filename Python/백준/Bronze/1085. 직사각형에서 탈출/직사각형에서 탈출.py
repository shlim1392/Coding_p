def solution(x, y, w, h):
    dl = x
    dr = w - x
    db = y
    dt = h -y
    min_d = min(dl, dr, db, dt)
    return min_d

x, y, w, h = map(int, input().split())
print(solution(x,y,w,h))