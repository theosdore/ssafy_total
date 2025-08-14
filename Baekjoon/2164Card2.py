import sys

from collections import deque

N = int(input())
cards = deque([i for i in range(1, N+1)])

while len(cards) >= 2:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])

"""
8 4 2 0
"""