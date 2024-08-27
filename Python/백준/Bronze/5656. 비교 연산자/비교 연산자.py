def solution():
    case_num = 1
    
    while True:
        a, op, b = input().split()
        a = int(a)
        b = int(b)

        if op == "E":
            break
        
        if op == ">":
            result = a > b
        elif op == ">=":
            result = a >= b
        elif op == "<":
            result = a < b
        elif op == "<=":
            result = a <= b
        elif op == "==":
            result = a == b
        elif op == "!=":
            result = a != b
        
        print(f"Case {case_num}: {'true' if result else 'false'}")
        case_num += 1

solution()
