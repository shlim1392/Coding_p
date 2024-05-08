def solution(sizes):
    normalized_sizes = [[max(size), min(size)] for size in sizes]
    max_width = max(size[0] for size in normalized_sizes)
    max_height = max(size[1] for size in normalized_sizes)
    answer = max_width * max_height
    return answer
