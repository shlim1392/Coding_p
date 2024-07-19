def solution(a):
    if a == list(range(1, 9)):
        print("ascending")
    elif a == list(range(8, 0, -1)):
        print("descending")
    else:
        print("mixed")

a = list(map(int, input().split()))
solution(a)
