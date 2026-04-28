import sys
input = lambda: sys.stdin.readline().rstrip()

class Node:
    def __init__(self, inp, flag=None) -> None:
        self.inp = inp
        self.flag = flag
        self.child = {}

class Trie:
    def __init__(self) -> None:
        self.head = Node(None)
    
    def insert(self, string):
        curNode = self.head
        
        for char in string:
            if char not in curNode.child:
                curNode.child[char] = Node(char)
            
            curNode = curNode.child[char]
        
        curNode.flag = True
    
    def search(self, string):
        curNode = self.head
        cnt = 0
        
        for char in string:
            curNode = curNode.child[char]
            if len(curNode.child) > 1 or curNode.flag:
                cnt += 1
        
        return cnt

while True:
    try: N = int(input())
    except: break
    
    di = Trie()
    word = []
    for _ in range(N):
        di.insert(s := input())
        word.append(s)
    cnt = 0
    for w in word:
        cnt += di.search(w)
    
    print(f"{cnt/N:.2f}")