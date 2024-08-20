def solution():
    X = input().strip()
    count = 0
    
    while len(X) > 1:
        X = str(sum(int(digit) for digit in X))
        count += 1
    
    print(count)
    if int(X) % 3 == 0:
        print("YES")
    else:
        print("NO")

solution()