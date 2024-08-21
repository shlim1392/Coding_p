def solution():
    N, M = map(int, input().split())
    stores = list(map(int, input().split()))
    
    brand_count = [0] * (M + 1)
    
    for store in stores:
        brand_count[store] += 1
    
    min_required_people = max(brand_count)
    print(min_required_people)


solution()
