import sys
sys.stdin = open("C:\\Users\\SSAFY\\Desktop\\Aiden\\swea\\stack_and_recursion2\\input.txt")

from collections import deque

for t in range(1, int(input())+1):
    N = int(input())
    mapmap = [list(map(int, input())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]
    startpoint = [-1, -1]
    for i in range(N):
        if 2 in mapmap[i]:
            startpoint = [i, mapmap[i].index(2)]
    que = deque([startpoint])
    dlt = [(i,0)for i in [1, -1]] + [(0,i)for i in [1, -1]]

    result = 0
    while True:
        current_pos = que.popleft()
        visited[current_pos[0]][current_pos[1]] = True
        for i in range(4):
            temp_x = current_pos[0]+dlt[i][0]
            temp_y = current_pos[1]+dlt[i][1]
            if temp_x < 0 or temp_x >= N or temp_y < 0 or temp_y >= N:
                continue
            else:
                if mapmap[temp_x][temp_y] == 0 and visited[temp_x][temp_y]== False:
                    que.append((temp_x, temp_y))
                elif mapmap[temp_x][temp_y] == 3:
                    result = 1
                    break
        if len(que) == 0:
            break
    
    print(f"#{t} {result}")

