def solution(arr, idx):
    min_idx = []
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            min_idx.append(i)
    if min_idx:
        return min(min_idx)
    else:
        return -1