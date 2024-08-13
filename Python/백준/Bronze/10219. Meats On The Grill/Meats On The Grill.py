def main():
    T = int(input())
    for _ in range(T):
        H, W = map(int, input().split())
        for _ in range(H):
            s = input()
            print(s[::-1])

if __name__ == "__main__":
    main()
