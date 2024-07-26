def find_median_of_three(x, y, z):
    return sorted([x, y, z])[1]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    
    k = list(map(int, data[1:n+1]))
    a = list(map(int, data[n+1:2*n+1]))
    b = list(map(int, data[2*n+1:3*n+1]))
    
    result = []
    
    for i in range(n):
        median_distance = find_median_of_three(k[i], a[i], b[i])
        result.append(median_distance)
    
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
