def max_t_for_d(d):
    t = 0
    while (t + t * t) <= d:
        t += 1
    return t - 1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        d = int(data[i])
        results.append(max_t_for_d(d))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
