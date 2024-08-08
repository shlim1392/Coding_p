a = int(input())  
b = int(input())  
c = int(input())  
d = int(input()) 
e = int(input()) 
f = int(input()) 

sci = [a, b, c, d]
sci.sort(reverse=True)
sci_sum = sum(sci[:3])

soc = max(e, f)

total = sci_sum + soc

print(total)

        
        