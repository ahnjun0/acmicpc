table = {"A":4,"B":3,"C":2,"D":1,"F":0,"P":0}
all_score = 0
all_credit = 0

for _ in range(20):
    _, credit, score = input().split()
    all_score += (table[score[0]] + (0.5 if score[-1] == "+" else 0)) * float(credit)
    all_credit += float(credit) if score[0] != "P" else 0
    
print(all_score / all_credit)