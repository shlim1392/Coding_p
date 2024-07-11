def calculate_difficulty(emoji):
    length = len(emoji)
    colons = emoji.count(':')
    underscores = emoji.count('_')
    
    difficulty = length + colons + underscores * 5
    return difficulty


emoji = input().strip()


difficulty = calculate_difficulty(emoji)
print(difficulty)
