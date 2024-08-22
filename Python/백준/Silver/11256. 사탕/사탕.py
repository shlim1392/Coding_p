def solution():
    T = int(input())
    
    for _ in range(T):
        J, N = map(int, input().split())
        box_sizes = []
        for _ in range(N):
            R, C = map(int, input().split())
            box_sizes.append(R * C)
        
        box_sizes.sort(reverse=True)
        used_boxes = 0
        for size in box_sizes:
            J -= size
            used_boxes += 1
            if J <= 0:
                break
        print(used_boxes)

solution()