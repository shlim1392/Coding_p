def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    logs = data[1:]

    current_people = set()

    for log in logs:
        name, action = log.split()
        if action == "enter":
            current_people.add(name)
        elif action == "leave":
            current_people.remove(name)

    for person in sorted(current_people, reverse=True):
        print(person)

main()
