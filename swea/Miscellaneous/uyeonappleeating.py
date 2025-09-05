import sys
sys.stdin = open('ssafy_total\swea\Miscellaneous\input.txt')

for t in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    targetlst = []
    dlt = [(0,1), (1,0),(0,-1), (-1,0)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                targetlst.append((arr[i][j], i, j))

    targetlst.sort(key=lambda x:x[0], reverse=True)
    currentPos = [0,0]
    dltC = 0
    result = 0
    while targetlst:
        tempPos = targetlst.pop()
        currentPos
    print(f"#{t} {result}")
    
    
    