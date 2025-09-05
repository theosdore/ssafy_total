
N, M = map(int, input().split())
lst = []
def recur(cnt, prev):
    if cnt == M:
        print(*lst)
        return
    for i in range(prev, N+1):
        lst.append(i)
        recur(cnt+1, i)
        lst.pop()

recur(0, 1)