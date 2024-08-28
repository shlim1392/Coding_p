def solution(name, yearning, photo):
    yearning_dict = {name[i]: yearning[i] for i in range(len(name))}
    result = []
    for persons in photo:
        score = 0
        for person in persons:
            score += yearning_dict.get(person, 0)  
        result.append(score)
    
    return result
