def solution(n):
    answer = 0 
    for x in range(1, n+1):
        div = []
        for i in range(1, x+1):
            if x % i == 0:
                div.append(i)
        if len(div) >= 3:
            answer += 1                
    return answer