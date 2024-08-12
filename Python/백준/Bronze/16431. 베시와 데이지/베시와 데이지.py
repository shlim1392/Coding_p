Br, Bc = map(int, input().split())
Dr, Dc = map(int, input().split())
Jr, Jc = map(int, input().split())


bessie_time = max(abs(Br - Jr), abs(Bc - Jc))

daisy_time = abs(Dr - Jr) + abs(Dc - Jc)

if bessie_time < daisy_time:
    print("bessie")
elif daisy_time < bessie_time:
    print("daisy")
else:
    print("tie")
