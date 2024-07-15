def last_digit_computer(a, b):
    if b == 0:
        return 1
    a = a % 10
    pattern = {
        0: [10],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }
    pattern_list = pattern[a]
    return pattern_list[(b % len(pattern_list)) - 1]

def solution(n):
    results = []
    for _ in range(n):
        a, b = map(int, input().split())
        results.append(last_digit_computer(a, b))
    for result in results:
        print(result)

n = int(input())
solution(n)
