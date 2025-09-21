import sys
sys.stdin = open("C:\\Programming\\SSAFY_TOTAL\\swea\\bruteforceAndBacktracking\\input.txt")

def recur(n):
    global counter
    global result
    global tempresult
    for i in range(N):
        if tempresult >= result:
            return
        if counter == N-1:
            tempresult += arr[n][0]
            if tempresult < result:
                result = tempresult
            tempresult -= arr[n][0]
            return
        if not visited[i]:
            tempresult += arr[n][i]
            visited[i] = True
            counter += 1
            recur(i)
            counter -= 1
            tempresult -= arr[n][i]
            visited[i] = False
            
        
for t in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False]*N
    result = 1000
    tempresult = 0
    counter = 0
    visited[0] = True
    recur(0)
    print(f"#{t} {result}")