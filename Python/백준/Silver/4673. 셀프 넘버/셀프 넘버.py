def d(n):
    return n + sum(int(digit) for digit in str(n))

def find_self_numbers(limit):
    generated = set()
    
    for i in range(1, limit + 1):
        generated.add(d(i))
    
    for i in range(1, limit + 1):
        if i not in generated:
            print(i)

find_self_numbers(10000)
