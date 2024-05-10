def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    numerator = numer1 * denom2 + numer2 * denom1
    denominator = denom1 * denom2
    gcd_val = gcd(numerator, denominator)
    return [numerator // gcd_val, denominator // gcd_val]