import sys
input = sys.stdin.read

def main():
    data = input().strip().split()
    i = 0
    while True:
        a = int(data[i])
        b = int(data[i+1])
        if a == 0 and b == 0:
            break
        if a > b:
            print("Yes")
        else:
            print("No")
        i += 2

if __name__ == "__main__":
    main()
