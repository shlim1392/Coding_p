days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


x, y = map(int, input().split())


weekdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]


total_days = y - 1  
for i in range(x - 1):
    total_days += days_in_month[i]


day_of_week = (total_days % 7)  


print(weekdays[day_of_week])
