def heating_time(A, B, C, D, E):
    if A < 0:
        time_to_heat_to_zero = abs(A) * C
        time_to_defrost = D
        time_to_heat_to_B = B * E
        total_time = time_to_heat_to_zero + time_to_defrost + time_to_heat_to_B
    else:
        total_time = (B - A) * E
    
    return total_time

A = int(input().strip())
B = int(input().strip())
C = int(input().strip())
D = int(input().strip())
E = int(input().strip())

print(heating_time(A, B, C, D, E))
