def check_multiples():
    n = int(input().strip())
    
    while True:
        num = int(input().strip())
        
        if num == 0:
            break
        
        if num % n == 0:
            print(f"{num} is a multiple of {n}.")
        else:
            print(f"{num} is NOT a multiple of {n}.")

check_multiples()
