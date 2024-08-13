N, L = map(int, input().split())

t = 0  
pos = 0  

for _ in range(N):
    D, R, G = map(int, input().split())
    
    t += D - pos 
    pos = D
    
    cycle = t % (R + G)  
    
    if cycle < R: 
        t += R - cycle

t += L - pos  

print(t)
