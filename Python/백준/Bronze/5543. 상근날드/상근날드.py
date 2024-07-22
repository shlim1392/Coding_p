# 가격 입력 받기
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

burgers = [a, b, c]
drinks = [d, e]

min_set_price = float('inf')

for burger in burgers:
    for drink in drinks:
        set_price = burger + drink - 50
        if set_price < min_set_price:
            min_set_price = set_price

print(min_set_price)
