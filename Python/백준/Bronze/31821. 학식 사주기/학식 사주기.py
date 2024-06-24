def solution(menu, order):
    price = 0
    for i in order:
        price += menu[i-1]
    return price

n = int(input())
menu = [int(input()) for _ in range(n)]
m = int(input())
order = [int(input()) for _ in range(m)]

print(solution(menu, order))


    
