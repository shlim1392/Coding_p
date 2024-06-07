def solution(my_string):
    numbers = [int(x) for x in my_string if x.isdigit()]
    sorted_numbers = sorted(numbers)
    return sorted_numbers