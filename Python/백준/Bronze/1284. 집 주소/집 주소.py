while True:
    n = input()
    if n == '0':
        break
    width = 2  
    for digit in n:
        if digit == '1':
            width += 2
        elif digit == '0':
            width += 4
        else:
            width += 3
        width += 1  
    width -= 1  
    print(width)
