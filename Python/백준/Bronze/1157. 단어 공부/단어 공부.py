from collections import Counter

s = input().upper()
counter = Counter(s)

most = counter.most_common(2)
if len(most) > 1 and most[0][1] == most[1][1]:
    print('?')
else:
    print(most[0][0])