N, M = map(int, input().split())
totalTime = 0
path = []
def recur(cnt):
    if cnt == M:
        print(*path)
    for i in range(1, N+1):
        if i not in path:
            path.append(i)
            recur(cnt+1)
            path.pop()
recur(0)