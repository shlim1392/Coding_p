resistor_values = {
    'black': (0, 1),
    'brown': (1, 10),
    'red': (2, 100),
    'orange': (3, 1000),
    'yellow': (4, 10000),
    'green': (5, 100000),
    'blue': (6, 1000000),
    'violet': (7, 10000000),
    'grey': (8, 100000000),
    'white': (9, 1000000000)
}

first_color = input().strip()
second_color = input().strip()
third_color = input().strip()

first_digit = resistor_values[first_color][0]
second_digit = resistor_values[second_color][0]
multiplier = resistor_values[third_color][1]

resistance_value = (first_digit * 10 + second_digit) * multiplier

print(resistance_value)
