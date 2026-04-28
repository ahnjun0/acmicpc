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
        
        for char in string:
            if char in curNode.child:
                curNode = curNode.child[char]
            else:
                return False
        
        return True if curNode.flag and not curNode.child else False


for _ in range(int(input())):
    phoneBook = Trie()
    
    inp = []
    for _ in range(int(input())):
        testc = input()
        inp.append(testc)
        phoneBook.insert(testc)
    
    yesCase = True
    for val in inp:
        if not phoneBook.search(val):
            yesCase = False
            break
    
    print("YES" if yesCase else "NO")