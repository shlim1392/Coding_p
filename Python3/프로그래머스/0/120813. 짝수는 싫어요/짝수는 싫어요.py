def solution(n):
    answer = sorted([x for x in range(n+1) if x % 2 ==1])
    return answer