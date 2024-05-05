def solution(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    def lcm(x, y):
        return x * y // gcd(x, y)
    
    return [gcd(a, b), lcm(a, b)]
