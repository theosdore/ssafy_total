import sys

sys.stdin = open("../binarySearch/input.txt")

from collections import deque
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    if N == M:
        print(f"#{t} 0")
        continue
    result = 0
    que = deque()
    que.append((N, 0))
    setset = {N}

    while que:
        tempN = que.popleft()
        if tempN[0] == M:
            result = tempN[1]
            break
        else:
            s = tempN[0] - 1
            a = tempN[0] + 1
            d = tempN[0] * 2
            if s not in setset and s >= 0:
                setset.add(s)
                que.append((s, tempN[1] + 1))
            if a not in setset and a <= M:
                setset.add(a)
                que.append((a, tempN[1] + 1))
            if d not in setset and d < 2*M:
                setset.add(d)
                que.append((d, tempN[1] + 1))

    print(f"#{t} {result}")
