def solution(numbers, num1, num2):
    answer = []
    for x in numbers[num1:num2+1]:
        answer.append(x)
    return answer