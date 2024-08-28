def solution(a, b, n):
    total_cola = 0
    
    while n >= a:
        new_cola = (n // a) * b
        total_cola += new_cola
        n = new_cola + (n % a)  
        
    return total_cola
