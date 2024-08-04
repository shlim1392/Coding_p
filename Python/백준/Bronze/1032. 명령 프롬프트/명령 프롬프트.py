def find_pattern():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    filenames = data[1:]

    pattern = list(filenames[0])

    for filename in filenames[1:]:
        for i in range(len(pattern)):
            if pattern[i] != filename[i]:
                pattern[i] = '?'

    print(''.join(pattern))

find_pattern()
