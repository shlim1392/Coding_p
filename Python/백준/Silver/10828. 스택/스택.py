import sys
input = sys.stdin.readline

def solution():
    stack = []
    N = int(input().strip())
    
    for _ in range(N):
        cmd = input().strip()
        
        if cmd.startswith("push"):
            _, x = cmd.split()
            stack.append(int(x))
        elif cmd == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif cmd == "size":
            print(len(stack))
        elif cmd == "empty":
            print(1 if not stack else 0)
        elif cmd == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)

solution()