for t in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [True] + [False]*(N-1)
    level = 0
    printlst = [0]*3
    print(f"#{t}")
    def recur(x):
        global level

        if level ==2:
            print(*printlst)
            return
        for i in range(N):
            if arr[x][i] == 1 and not visited[i]:
                level += 1
                visited[i] = True
                printlst[level] = i
                recur(i)
                level -= 1
                visited[i] = False
    recur(0)
