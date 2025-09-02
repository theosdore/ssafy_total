import sys
sys.stdin = open("ssafy_total\swea\queue\input.txt")

from collections import deque
dlt = [(0,1), (0,-1), (1,0), (-1,0)]

for t in range(1, int(input())+1):
    queue = deque()
    N, M = map(int,input().split())
    result = [[0]*M for _ in range(N)]
    arr = [input() for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "W":
                queue.append((i,j))
    while queue:
        findpos = queue.popleft()
        for i in range(4):
            changedX = findpos[0] + dlt[i][0] 
            changedY = findpos[1] + dlt[i][1]
            if 0 <= changedX < N and 0 <= changedY < M and result[changedX][changedY] == 0 and arr[changedX][changedY] != "W":
                queue.append((changedX, changedY))
                result[changedX][changedY] = result[findpos[0]][findpos[1]] + 1
    
    finalR = 0
    for a in result:
        finalR += sum(a)
    print(f"#{t} {finalR}")
                
        