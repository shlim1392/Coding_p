def min_sets_for_room_number(room_number):
    count = [0] * 10

    for digit in room_number:
        count[int(digit)] += 1


    six_nine_count = count[6] + count[9]
    count[6] = count[9] = (six_nine_count + 1) // 2

    return max(count)

room_number = input().strip()

print(min_sets_for_room_number(room_number))
