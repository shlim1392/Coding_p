import sys

def solution():
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    members = []

    for i in range(1, n + 1):
        age, name = data[i].split()
        age = int(age)
        members.append((age, name))

    members.sort(key=lambda x: x[0])

    for age, name in members:
        print(age, name)


solution()
