def solution(hp):
    answer = hp // 5  
    remainder = hp % 5  
    answer += remainder // 3
    remainder = remainder % 3
    answer += remainder
    return answer