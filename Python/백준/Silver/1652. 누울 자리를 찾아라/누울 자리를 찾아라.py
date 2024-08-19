def solution():
    N = int(input())
    room = [input().strip() for _ in range(N)]
    
    horizontal_count = 0
    for row in room:
        empty_space = 0
        for cell in row:
            if cell == '.':
                empty_space += 1
            else:
                if empty_space >= 2:
                    horizontal_count += 1
                empty_space = 0
        if empty_space >= 2:  
            horizontal_count += 1
    
    vertical_count = 0
    for col in range(N):
        empty_space = 0
        for row in range(N):
            if room[row][col] == '.':
                empty_space += 1
            else:
                if empty_space >= 2:
                    vertical_count += 1
                empty_space = 0
        if empty_space >= 2:  
            vertical_count += 1
    
    print(horizontal_count, vertical_count)

solution()
