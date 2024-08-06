def count_strings_in_set():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    M = int(data[1])

    S = set(data[2:2+N])
    check_strings = data[2+N:2+N+M]

    count = 0
    for string in check_strings:
        if string in S:
            count += 1

    print(count)

if __name__ == "__main__":
    count_strings_in_set()
