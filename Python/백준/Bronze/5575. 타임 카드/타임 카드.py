def to_sec(h, m, s):
    return h * 3600 + m * 60 + s

def to_hms(sec):
    h = sec // 3600
    m = (sec % 3600) // 60
    s = (sec % 3600) % 60
    return h, m, s


for _ in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())
    
    start = to_sec(sh, sm, ss)
    end = to_sec(eh, em, es)
    
    work_sec = end - start
    h, m, s = to_hms(work_sec)
    
    print(h, m, s)
