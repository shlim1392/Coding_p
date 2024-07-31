def symmetric_difference_count():

    a_size, b_size = map(int, input().split())
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))
    
    symmetric_diff = set_a.symmetric_difference(set_b)
    print(len(symmetric_diff))

symmetric_difference_count()
