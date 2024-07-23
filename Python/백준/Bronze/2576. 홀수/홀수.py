numbers = [int(input().strip()) for _ in range(7)]

odd_numbers = [num for num in numbers if num % 2 != 0]

if odd_numbers:
    total_sum = sum(odd_numbers)
    min_value = min(odd_numbers)
    print(total_sum)
    print(min_value)
else:
    print(-1)
