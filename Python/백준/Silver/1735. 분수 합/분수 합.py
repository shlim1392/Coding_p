import math

def solution():
    A1, B1 = map(int, input().split())
    A2, B2 = map(int, input().split())

    numerator = A1 * B2 + A2 * B1
    denominator = B1 * B2
    gcd_value = math.gcd(numerator, denominator)
    numerator //= gcd_value
    denominator //= gcd_value
    print(numerator, denominator)

solution()
