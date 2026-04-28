import sys
input = lambda: sys.stdin.readline().rstrip()

class Node:
    def __init__(self, char) -> None:
        self.char = char
        self.child = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self) -> None:
        self.head = Node(None)

    def insert(self, string):
        curNode = self.head
        for char in string:
            if char not in curNode.child:
                curNode.child[char] = Node(char)
            curNode = curNode.child[char]
        curNode.is_end_of_word = True

    def count_leaf_nodes(self, node):
        if not node.child:
            return 1
        count = 0
        for child in node.child.values():
            count += self.count_leaf_nodes(child)
        return count

trie = Trie()
n = int(input())
for _ in range(n):
    trie.insert(input())

print(trie.count_leaf_nodes(trie.head))