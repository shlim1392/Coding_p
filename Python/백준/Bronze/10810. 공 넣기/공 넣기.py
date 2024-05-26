n, m = map(int, input().split())  
num = [0] * (n+1) 

for _ in range(m):
    i, j, k = map(int, input().split()) 
    for index in range(i, j+1):  
        num[index] = k 

print(' '.join(map(str, num[1:]))) 