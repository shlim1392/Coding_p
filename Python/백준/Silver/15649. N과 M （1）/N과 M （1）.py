import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = []
used = [False] * (N + 1)
out_lines = []

def dfs():
    if len(seq) == M:
        out_lines.append(" ".join(map(str, seq)))
        return
    for x in range(1, N + 1):
        if not used[x]:
            used[x] = True
            seq.append(x)
            dfs()
            seq.pop()
            used[x] = False

dfs()
print("\n".join(out_lines))
