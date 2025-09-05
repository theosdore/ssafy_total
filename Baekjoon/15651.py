
N, M = map(int, input().split())
lst = []
def recur(cnt):
    if cnt == M:
        print(*lst)
        return
    for i in range(1, N+1):
        lst.append(i)
        recur(cnt+1)
        lst.pop()

recur(0)