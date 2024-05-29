def convert(a, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while a > 0:
        res = digits[a % b] + res
        a //= b
    return res

a, b = map(int, input().split())
print(convert(a, b))
