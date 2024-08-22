def solution():
    n = int(input())
    s = input().strip()
    
    count_2 = s.count('2')
    count_e = s.count('e')

    if count_2 > count_e:
        print("2")
    elif count_e > count_2:
        print("e")
    else:
        print("yee")

solution()