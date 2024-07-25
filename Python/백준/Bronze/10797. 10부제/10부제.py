date = int(input().strip())
car_numbers = list(map(int, input().strip().split()))


violations = sum(1 for car in car_numbers if car == date)


print(violations)
