from collections import deque

deck = deque(list(range(1, int(input())+1)))
while(len(deck) > 1):
    deck.popleft()
    deck.append(deck.popleft())

print(deck[0])