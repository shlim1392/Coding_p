def solution(T):
    A, B, C = 300, 60, 10
    count_A, T = divmod(T, A)
    count_B, T = divmod(T, B)
    count_C, T = divmod(T, C)
    return f"{count_A} {count_B} {count_C}" if T == 0 else "-1"


T = int(input().strip())
print(solution(T))

