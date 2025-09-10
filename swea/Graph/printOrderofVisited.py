from collections import deque
for t in range( 1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    que = deque()
    que.append(0)
    visited = [False]*N
    visited[0] = True
    print(f"#{t}", end=" ")
    while que:
        tempQ = que.popleft()
        print(tempQ, end= " ")
        for i in range(N):
            if arr[tempQ][i] == 1 and not visited[i]:
                visited[i] = True
                que.append(i)
    print("")