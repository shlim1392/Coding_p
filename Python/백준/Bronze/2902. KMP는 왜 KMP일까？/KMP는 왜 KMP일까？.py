def solution():
    long_name = input().strip()
    
    parts = long_name.split('-')
    
    short_name = ''.join([part[0] for part in parts])
    
    print(short_name)

solution()
