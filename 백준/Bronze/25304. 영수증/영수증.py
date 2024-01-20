R = int(input())
T = int(input())

res = 0

for _ in range(T):
    a, b = map(int, input().split())
    res += (a * b)
    

if res == R:
    print("Yes")
else : 
    print("No")