def solution(N, A, B, C):
    total_supervisors = 0

    for i in range(N):
        students = A[i]
        total_supervisors += 1
        remaining_students = students - B

        if remaining_students > 0:
            
            total_supervisors += (remaining_students + C - 1) // C

    return total_supervisors


N = int(input().strip())
A = list(map(int, input().strip().split()))
B, C = map(int, input().strip().split())

print(solution(N, A, B, C))
