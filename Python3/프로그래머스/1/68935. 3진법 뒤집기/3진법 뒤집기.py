def solution(n):    
    if n == 0:
        return '0'
    digits = ''
    decimal = 0
    while n > 0:
        digits = str(n % 3) + digits
        n = n // 3    
        
    res_b = digits[::-1]
    for i, value in enumerate(reversed(res_b)):
        decimal += int(value) * (3**i)
    return decimal
    
