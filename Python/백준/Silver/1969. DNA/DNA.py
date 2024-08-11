# 입력 처리
N, M = map(int, input().split())
dna_list = [input() for _ in range(N)]

# 결과 DNA와 최소 Hamming Distance 합 계산
result_dna = ""
min_hamming_sum = 0

for i in range(M):
    count = {"A": 0, "C": 0, "G": 0, "T": 0}
    
    for dna in dna_list:
        count[dna[i]] += 1
    
    most_common = min(count, key=lambda x: (-count[x], x))
    result_dna += most_common
    
    min_hamming_sum += sum(1 for dna in dna_list if dna[i] != most_common)

print(result_dna)
print(min_hamming_sum)
