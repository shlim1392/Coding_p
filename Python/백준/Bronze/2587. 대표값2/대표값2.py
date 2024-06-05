num = [int(input()) for _ in range(5)]
num.sort()  

mean = sum(num) // len(num)  

if len(num) % 2 == 1:
    median = num[len(num) // 2]
else:
    median = (num[len(num) // 2 - 1] + num[len(num) // 2]) / 2

print(mean)
print(median)
