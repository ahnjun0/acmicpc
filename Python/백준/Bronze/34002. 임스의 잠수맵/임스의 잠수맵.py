import sys
input = lambda: sys.stdin.readline()
imap = lambda: map(int, input().split())

exp = 0
minute = 0
flag = 0

A, B, C = imap()
S, V = imap()
L = int(input())

need_exp = (250 - L) * 100
S_exp = S * 30 * B
V_exp = V * 30 * C

minute += (30 * V) if need_exp > V_exp else (flag := (need_exp // C) + (1 if need_exp % C else 0))
if not flag:
    need_exp -= V_exp
    minute += (30 * S) if need_exp > S_exp else (flag := (need_exp // B) + (1 if need_exp % B else 0))

if not flag:
    need_exp -= S_exp
    minute += (need_exp // A) + (1 if need_exp % A else 0)

print(minute)