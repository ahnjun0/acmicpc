import sys
input = lambda : sys.stdin.readline().rstrip()

emptySet = [False] * 21

for _ in range(int(input())):
    order = input()
    
    match order[:2]:
        case "ad":
            emptySet[int(order[4:])] = True
            
        case "re":
            emptySet[int(order[7:])] = False
            
        case "ch":
            print(1 if emptySet[int(order[6:])] else 0)
            
        case "to":
                emptySet[int(order[7:])] = not emptySet[int(order[7:])]
        
        case "al":
            emptySet = [True] * 21
            
        case "em":
            emptySet = [False] * 21