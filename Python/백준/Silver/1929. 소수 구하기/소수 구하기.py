def sieve_of_eratosthenes(m, n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False 

    for start in range(2, int(n**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, n + 1, start):
                sieve[multiple] = False

    for num in range(m, n + 1):
        if sieve[num]:
            print(num)

m, n = map(int, input().split())

sieve_of_eratosthenes(m, n)
