def solution():
    n, k = map(int, input().split())
    
    students = [[0, 0] for _ in range(6)]  
    
    for _ in range(n):
        s, y = map(int, input().split())
        students[y - 1][s] += 1
    
    room = 0
    
    for i in range(6):
        for j in range(2):
            if students[i][j] > 0:
                room += students[i][j] // k
                if students[i][j] % k > 0:
                    room += 1

    print(room)

solution()
