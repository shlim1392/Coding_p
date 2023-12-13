def solution(todo_list, finished):
    return [x for x, i in zip(todo_list, finished) if not i]
    