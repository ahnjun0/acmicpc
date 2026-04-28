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
        
        return True

arr = Trie()
N, M = map(int, input().split())
for _ in range(N):
    arr.insert(input())

cnt = 0
for _ in range(M):
    if arr.search(input()):
        cnt += 1

print(cnt)