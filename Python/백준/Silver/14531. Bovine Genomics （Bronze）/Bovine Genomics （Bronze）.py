def solution():
    n, m = map(int, input().split())
    
    spotty = [input().strip() for _ in range(n)]
    plain = [input().strip() for _ in range(n)]
    
    count = 0
    
    for j in range(m):
        spotty_set = set(spotty[i][j] for i in range(n))
        plain_set = set(plain[i][j] for i in range(n))
        
        if spotty_set.isdisjoint(plain_set):
            count += 1
    
    print(count)

solution()
