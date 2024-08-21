def solution():
    while True:
        target = int(input())
        if target == 0:
            break
        
        low, high = 1, 50
        path = []
        
        while low <= high:
            mid = (low + high) // 2
            path.append(mid)
            
            if mid == target:
                break
            elif mid < target:
                low = mid + 1
            else:
                high = mid - 1
        
        print(" ".join(map(str, path)))

solution()
