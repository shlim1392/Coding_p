def count_cards(card_numbers, queries):
    card_count = {}
    
    for number in card_numbers:
        if number in card_count:
            card_count[number] += 1
        else:
            card_count[number] = 1
    
    result = []
    for query in queries:
        if query in card_count:
            result.append(card_count[query])
        else:
            result.append(0)
    
    return result

N = int(input())
card_numbers = list(map(int, input().split()))
M = int(input())
queries = list(map(int, input().split()))

result = count_cards(card_numbers, queries)

print(' '.join(map(str, result)))
