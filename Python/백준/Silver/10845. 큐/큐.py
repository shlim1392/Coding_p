from collections import deque
import sys
input = sys.stdin.read

def process_commands(commands):
    queue = deque()
    output = []

    for command in commands:
        if command.startswith("push"):
            _, value = command.split()
            queue.append(int(value))
        elif command == "pop":
            if queue:
                output.append(queue.popleft())
            else:
                output.append(-1)
        elif command == "size":
            output.append(len(queue))
        elif command == "empty":
            output.append(1 if not queue else 0)
        elif command == "front":
            if queue:
                output.append(queue[0])
            else:
                output.append(-1)
        elif command == "back":
            if queue:
                output.append(queue[-1])
            else:
                output.append(-1)

    return output


data = input().strip().split("\n")
N = int(data[0])
commands = data[1:]

results = process_commands(commands)

for result in results:
    print(result)
