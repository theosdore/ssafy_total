import sys

sys.stdin = open("input.txt")

from collections import deque

for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
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
            cnt = tempN[1] + 1
            s = tempN[0] - 1
            a = tempN[0] + 1
            d = tempN[0] * 2
            di = tempN[0] // 2
            if s not in setset and s >= 0:
                setset.add(s)
                que.append((s, cnt))
            if a not in setset and a <= 100000:
                setset.add(a)
                que.append((a, cnt))
            if d not in setset and d <= 100000 and d <= M*2:
                setset.add(d)
                que.append((d, cnt))
            if di not in setset:
                setset.add(di)
                que.append((di, cnt))

    print(f"#{t} {result}")
