def solution():
    while True:
        line = input().rstrip()
        if line == ".":
            break
        
        stack = []
        is_balanced = True
        
        for char in line:
            if char in "([":  
                stack.append(char)
            elif char == ")":
                if stack and stack[-1] == "(":
                    stack.pop()  
                else:
                    is_balanced = False
                    break
            elif char == "]":
                if stack and stack[-1] == "[":
                    stack.pop()  
                else:
                    is_balanced = False
                    break
        
        if is_balanced and not stack:
            print("yes")
        else:
            print("no")

solution()
