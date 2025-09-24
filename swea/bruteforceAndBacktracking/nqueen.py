import sys
sys.stdin = open("SSAFY_TOTAL\\swea\\bruteforceAndBacktracking\\input.txt")

def tovisit(i, j):
    global N
    for dlt in dltlst:
        x = i
        y = j
        while 0 <= x < N and  0 <= y < N:
            visited[x][y] += 1
            x += dlt[0]
            y += dlt[1]
    for a in range(N):
        visited[a][j] += 1
        visited[i][a] += 1
    visited[i][j] -= 5

def unvisit(i, j):
    global N
    for dlt in dltlst:
        x = i
        y = j
        while 0 <= x < N and  0 <= y < N:
            visited[x][y] -= 1
            x += dlt[0]
            y += dlt[1]
    for a in range(N):
        visited[a][j] -= 1
        visited[i][a] -= 1
    visited[i][j] += 5
    
def recur(n):
    global result
    global N
    if n == N:
        result += 1
        return
    for i in range(N):
        if not visited[i][n]:
            tovisit(i,n)
            recur(n + 1)
            unvisit(i,n)


for t in range(1, int(input())+1):
    N = int(input())
    visited = [[0]*N for _ in range(N)]
    dltlst = [(1,1), (1,-1), (-1,1), (-1,-1)]
    result = 0
    recur(0)
    print(f"#{t} {result}")

