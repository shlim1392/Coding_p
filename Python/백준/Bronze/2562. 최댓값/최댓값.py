max_val = 0  
max_index = 0  

for i in range(1, 10):  
    num = int(input())  
    if num > max_val:  
        max_val = num  
        max_index = i 

print(max_val)
print(max_index)