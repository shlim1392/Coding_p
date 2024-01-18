num1 = int(input())  # 세 자리 수 입력
num2 = int(input())  # 세 자리 수 입력

# 각 단계별 곱셈 결과 출력
for digit in str(num2)[::-1]:
    print(num1 * int(digit))
    
result = num1 * num2  # 두 수의 곱 계산
print(result)  # 곱셈 결과 출력