M = int(input())
belts = [tuple(map(int, input().split())) for _ in range(M)]


current_direction = 0 
current_rpm = 1 

for a, b, s in belts:
    if s == 1:
        current_direction = 1 - current_direction  
    
    current_rpm = current_rpm * b // a  

print(current_direction, current_rpm)
