while True:
    n = int(input())
    if n == -1:
        break
    
    div = []
    for d in range(1, n):
        if n % d == 0:
            div.append(d)
    
    if n == sum(div):
        res = ' + '.join(map(str, div))
        print(f'{n} = {res}')
    else:
        print(f'{n} is NOT perfect.')
