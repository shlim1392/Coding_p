c = input()
l = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for x in l:
    c = c.replace(x, '*')  

print(len(c))  
