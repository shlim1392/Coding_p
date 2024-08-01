def print_list(lst):
    print(" ".join(map(str, lst)))

wood_pieces = list(map(int, input().split()))

while wood_pieces != [1, 2, 3, 4, 5]:
    for i in range(4):
        if wood_pieces[i] > wood_pieces[i + 1]:
            wood_pieces[i], wood_pieces[i + 1] = wood_pieces[i + 1], wood_pieces[i]
            print_list(wood_pieces)
