def minimum_moves(N, M, J, apples):
    left = 1  
    right = M  
    moves = 0  

    for apple in apples:
        if apple > right:
            moves += apple - right
            left += apple - right
            right = apple
        elif apple < left:
            moves += left - apple
            right -= left - apple
            left = apple

    return moves


N, M = map(int, input().split())
J = int(input())
apples = [int(input()) for _ in range(J)]

result = minimum_moves(N, M, J, apples)
print(result)
