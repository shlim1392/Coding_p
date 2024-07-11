def swap_characters(s, a, b):
    s = list(s)  
    s[a], s[b] = s[b], s[a]  
    return ''.join(s)  


s = input()
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    s = swap_characters(s, a, b)

print(s)
