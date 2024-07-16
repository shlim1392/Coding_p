def is_vps(ps):
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

def solution(t, cases):
    results = []
    for case in cases:
        results.append(is_vps(case))
    return results


t = int(input())
cases = [input() for _ in range(t)]

results = solution(t, cases)
for result in results:
    print(result)
