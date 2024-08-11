w, h = map(int, input().split())
n = int(input())

h_cuts = [0, h]
v_cuts = [0, w]

for _ in range(n):
    d, p = map(int, input().split())
    if d == 0:  
        h_cuts.append(p)
    else:  
        v_cuts.append(p)


h_cuts.sort()
v_cuts.sort()

max_h = max(h_cuts[i+1] - h_cuts[i] for i in range(len(h_cuts) - 1))
max_w = max(v_cuts[i+1] - v_cuts[i] for i in range(len(v_cuts) - 1))

print(max_h * max_w)
