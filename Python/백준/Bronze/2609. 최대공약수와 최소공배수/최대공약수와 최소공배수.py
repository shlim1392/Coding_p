def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b, gcd_value):
    return (a * b) // gcd_value


a, b = map(int, input().split())
gcd_value = gcd(a, b)
lcm_value = lcm(a, b, gcd_value)

print(gcd_value)
print(lcm_value)
