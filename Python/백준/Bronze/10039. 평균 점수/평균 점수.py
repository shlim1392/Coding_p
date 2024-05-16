a = []

for _ in range(5):
    b = int(input())  
    if b < 40:  
        a.append(40)  
    else:
        a.append(b) 
avg = sum(a) / len(a)  
print(int(avg))