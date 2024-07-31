def max_passengers():
    current_passengers = 0
    max_passengers = 0

    for _ in range(4):
        out, in_ = map(int, input().split())
        current_passengers -= out
        current_passengers += in_
        if current_passengers > max_passengers:
            max_passengers = current_passengers

    print(max_passengers)


max_passengers()
