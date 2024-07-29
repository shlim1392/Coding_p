def octal_to_binary(octal_str):
    binary_str = ''.join(format(int(digit), '03b') for digit in octal_str)
    return binary_str.lstrip('0') or '0'

octal_str = input().strip()
print(octal_to_binary(octal_str))
