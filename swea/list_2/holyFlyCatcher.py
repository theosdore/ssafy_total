dtx = [-1, 1, 0, 0]
dty = [0, 0, 1, -1]
for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    max_kills = 0
    max_x = 0
    max_y = 0
    for i in range(n):
        for j in range(n):
            kills = arr[i][j]
            for k in range(4):
                if j + dtx[k] >= n or j + dtx[k] < 0 or i + dty[k] >= n or i + dty[k] < 0:
                    continue
                else:
                    kills += arr[i+dty[k]][j+dtx[k]]
            if kills > max_kills:
                max_kills, max_x, max_y = kills, i, j
    print(f"#{t+1} {max_kills} {max_x} {max_y}")
