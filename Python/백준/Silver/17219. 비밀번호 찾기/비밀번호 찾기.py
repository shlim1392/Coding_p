def solution():
    n, m = map(int, input().split())
    
    pw_dict = {}

    for _ in range(n):
        site, pw = input().split()
        pw_dict[site] = pw
    
    for _ in range(m):
        site = input().strip()
        print(pw_dict[site])

solution()
