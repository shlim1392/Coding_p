T = int(input())
n= 0
b= " "

for _ in range(T):
    n += 1
    print(b*(T-n)+"*"*n)