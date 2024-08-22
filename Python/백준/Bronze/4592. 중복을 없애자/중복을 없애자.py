def solution():
    while True:
        data = list(map(int, input().split()))
        if data[0] == 0: 
            break
        numbers = data[1:]
        result = []
        last_num = None
        for num in numbers:
            if num != last_num:
                result.append(num)
            last_num = num

        print(" ".join(map(str, result)) + " $")

solution()