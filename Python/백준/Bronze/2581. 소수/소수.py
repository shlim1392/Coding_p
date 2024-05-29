def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

m = int(input())
n = int(input())
res = []
for x in range(m, n+1): 
    if is_prime(x):
        res.append(x)
if len(res) == 0:  
    print(-1)
else:
    print(sum(res))
    print(min(res))
