def solution(arr1, arr2):
    if len(arr1) > len(arr2):
        return 1
    elif len(arr1) < len(arr2):
        return -1

    if sum(arr1) > sum(arr2):
        return 1
    elif sum(arr1) < sum(arr2):
        return -1

    return 0

def solution(arr1, arr2):
    return (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)) or (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1))

'''
1. (len(arr1) > len(arr2)) - (len(arr2) > len(arr1)): 이 부분은 두 배열의 길이를 비교하여 길이가 긴 쪽이 크면 1을 반환하고, 그렇지 않으면 -1을 반환합니다. 만약 길이가 같다면 0을 반환합니다.
2. (sum(arr1) > sum(arr2)) - (sum(arr2) > sum(arr1)): 이 부분은 두 배열의 원소 합을 비교하여 합이 큰 쪽이 크면 1을 반환하고, 그렇지 않으면 -1을 반환합니다. 만약 두 배열의 합이 같다면 0을 반환합니다.
3. or: 두 개의 조건을 결합합니다. 만약 첫 번째 조건이 참이면 해당 값을 반환하고, 그렇지 않으면 두 번째 조건의 값을 반환합니다.

'-' 연산자

(A > B) - (B > A):
만약 A가 B보다 크다면 (True) - (False)가 되어 결과는 1이 됩니다.
만약 B가 A보다 크다면 (False) - (True)가 되어 결과는 -1이 됩니다.
만약 A와 B가 같다면 (False) - (False)가 되어 결과는 0이 됩니다.

'''
