def solution():
    n = int(input())  
    count = 0
    seen = set()  

    for _ in range(n):
        line = input().strip()
        if line == "ENTER":
            seen.clear()  
        else:
            if line not in seen:
                count += 1
                seen.add(line) 
    print(count)

solution()
