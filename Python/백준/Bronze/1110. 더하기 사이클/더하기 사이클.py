def solution(N):
    original = N
    count = 0
    
    while True:
        count += 1
        tens = N // 10
        ones = N % 10
        sum_digits = tens + ones
        new_N = (ones * 10) + (sum_digits % 10)
        
        if new_N == original:
            break
        N = new_N
    
    return count


N = int(input())
print(solution(N))
