def count_digits(n, m, a, b):
    digit_counts = [0] * 10
    for i in range(n):
        for j in range(m):
            product = a[i] * b[j]
            for digit in str(product):
                digit_counts[int(digit)] += 1
    return digit_counts

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    results = []
    while index < len(data):
        n = int(data[index])
        m = int(data[index + 1])
        if n == 0 and m == 0:
            break
        index += 2
        a = list(map(int, data[index:index + n]))
        index += n
        b = list(map(int, data[index:index + m]))
        index += m
        digit_counts = count_digits(n, m, a, b)
        results.append(" ".join(map(str, digit_counts)))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
