import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
gestures = [input() for _ in range(n)]

wins_against = {'H': 'S', 'S': 'P', 'P': 'H'}

wins_from_start = {'H': [0]*n, 'S': [0]*n, 'P': [0]*n}
wins_from_end = {'H': [0]*n, 'S': [0]*n, 'P': [0]*n}

for i in range(n):
    for gesture in 'HSP':
        wins_from_start[gesture][i] = wins_from_start[gesture][i-1] + (1 if wins_against[gesture] == gestures[i] else 0)

for i in range(n-1, -1, -1):
    for gesture in 'HSP':
        if i < n-1:
            wins_from_end[gesture][i] = wins_from_end[gesture][i+1] + (1 if wins_against[gesture] == gestures[i] else 0)
        else:
            wins_from_end[gesture][i] = (1 if wins_against[gesture] == gestures[i] else 0)

max_wins = 0
for i in range(n+1):
    for gesture1 in 'HSP':
        for gesture2 in 'HSP':
            if i == 0:
                max_wins = max(max_wins, wins_from_end[gesture2][0])
            elif i == n: 
                max_wins = max(max_wins, wins_from_start[gesture1][n-1])
            else:
                total_wins = wins_from_start[gesture1][i-1] + wins_from_end[gesture2][i]
                max_wins = max(max_wins, total_wins)

print(max_wins)