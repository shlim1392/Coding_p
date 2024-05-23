try:
    while True:
        line = input()
        if line == "": 
            break
        print(line)
except EOFError:
    pass