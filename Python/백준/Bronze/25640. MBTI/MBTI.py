def solution(mbti_list, jin):
    res = 0
    for x in mbti_list:
        if jin == x:
            res += 1
    return res


jin = input()
n = int(input())
mbti_list = [input() for _ in range(n)]

print(solution(mbti_list, jin))
