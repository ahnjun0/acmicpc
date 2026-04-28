import sys
input = lambda: [*sys.stdin.readline().rstrip()]

exp = input()
stack = []
answer = ""

for x in exp:
    if "A" <= x <= "Z":
        answer += x
        continue
    
    if x == "(":
        stack.append(x)
    
    elif x == ")":
        while stack:
            if stack[-1] == "(":
                stack.pop()
                break
            answer += stack.pop()
    
    elif x in "+-":
        while stack and stack[-1] != "(": answer += stack.pop()
        stack.append(x)
    
    else:
        while stack and stack[-1] in "*/": answer += stack.pop()
        stack.append(x)

while stack: answer += stack.pop()
print(answer)