import sys
input = sys.stdin.read

def main():
    data = input().splitlines()
    
    initial_string = data[0]
    m = int(data[1])
    commands = data[2:]
    
    left_stack = list(initial_string)
    right_stack = []
    
    for command in commands:
        if command[0] == 'L':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif command[0] == 'D':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif command[0] == 'B':
            if left_stack:
                left_stack.pop()
        elif command[0] == 'P':
            left_stack.append(command[2])
    

    print(''.join(left_stack + list(reversed(right_stack))))

if __name__ == "__main__":
    main()
