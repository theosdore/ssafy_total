from collections import deque
import sys
sys.stdin = open("ssafy_total\swea\queue\input.txt")

queue = deque()
for _ in range(int(input())):
    lst = input().split()
    if lst[0] == "enqueue":
        queue.append(lst[1])
    elif lst[0] == "front":
        print(queue[0] if queue else -1)
    elif lst[0] == "rear":
        print(queue[-1] if queue else -1)
    elif lst[0] == "dequeue":
        print(queue.popleft() if queue else -1)
    elif lst[0] == "size":
        print(len(queue ))
    elif lst[0] == "isEmpty":
        print(-1 if queue else 1)