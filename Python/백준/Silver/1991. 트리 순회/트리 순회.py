import sys
from collections import deque
input = lambda: sys.stdin.readline()

class Node:
    def __init__(self, item, left, right) -> None:
        self.item = item
        self.left = left
        self.right = right

    # def __repr__(self) -> str:
    #     return f"{self.left} / {self.item} \\ {self.right}"

    
tree = {a : Node(a, b, c) for a, b, c in (input().split() for _ in range(int(input())))}

def order(node: Node, idx):
    if idx == 1: print(node.item, end='')
    if node.left != '.': order(tree[node.left], idx)
    if idx == 2: print(node.item, end='')
    if node.right != '.': order(tree[node.right], idx)
    if idx == 3: print(node.item, end='')

for i in range(1, 4):
    order(tree['A'], i)
    print()