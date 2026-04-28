import sys

input = lambda: int(sys.stdin.readline().rstrip())

n = input()
stack = []
cnt = 1
answer = []

for _ in range(n):
    num = input()

    if num > cnt:
        while True:
            stack.append(cnt)
            answer.append("+")
            cnt += 1

            if num == cnt:
                break

    if num < cnt:
        if stack[-1] == num:
            answer.append("-")
            del stack[-1]

        else:
            answer.append("NO")

    if num == cnt:
        answer.append("+")
        answer.append("-")
        cnt += 1

if "NO" not in answer:
    for k in answer:
        print(k)

else:
    print("NO")