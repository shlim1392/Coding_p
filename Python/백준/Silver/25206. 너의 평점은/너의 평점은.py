grades = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
tot_c = 0
tot_s = 0
for _ in range(20):
    c, score, grade = map(str, input().split())
    if grade == "P":
        continue
    else :
        score = float(score)
        credit = grades.get(grade)
        tot_c += (score * credit)
        tot_s += score
print(float(tot_c/tot_s))