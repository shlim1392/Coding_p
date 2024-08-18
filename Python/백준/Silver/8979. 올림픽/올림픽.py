def solution():
    n, k = map(int, input().split())
    countries = []

    for _ in range(n):
        country_info = list(map(int, input().split()))
        countries.append(country_info)

    countries.sort(key=lambda x: (-x[1], -x[2], -x[3]))

    rank = 1  
    result_rank = 0

    for i in range(n):
        if i > 0:
            if countries[i][1:] != countries[i-1][1:]:
                rank = i + 1

        if countries[i][0] == k:
            result_rank = rank
            break

    print(result_rank)

solution()
