import sys

def solution():
    input = sys.stdin.read
    data = input().split()  
    n = int(data[0])  
    numbers = list(map(int, data[1:n+1]))  
    
    numbers.sort(reverse=True) 
    
    sys.stdout.write('\n'.join(map(str, numbers)) + '\n')  

solution()
