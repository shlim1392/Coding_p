def digit_root(n):
    while n >= 10:  
        n = sum(int(digit) for digit in str(n))  
    return n

while True:
    n = int(input())
    if n == 0:
        break
    print(digit_root(n))
