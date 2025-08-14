# import sys
# sys.stdin = open("sample_input.txt")
for t in range(int(input())):
    # n 세로, m 가로
    n, m = map(int, input().split())
    # k 폭발 범위
    k = int(input())
    # 델타
    dlx = [0, 0, 1, -1]
    dly = [1, -1, 0, 0]
    # 폭탄지도
    arr = [list(input()) for _ in range(n)]

    # 순회 하면서 폭탄 확인
    for i in range(n):
        for j in range(m):
            if arr[i][j] == "@":
                arr[i][j] = "%"
                for p in range(4):
                    for q in range(1, k+1):
                        temp_x = j + dlx[p] * q
                        temp_y = i + dly[p] * q
                        if temp_x < 0 or temp_x == m or temp_y < 0 or temp_y == n:
                            break
                        elif arr[temp_y][temp_x] == "#" or arr[temp_y][temp_x] == "@" or arr[temp_y][temp_x] == "%":
                            break
                        else:
                            arr[temp_y][temp_x] = "%"

    print(f"#{t + 1}")
    for i in range(n):
        for j in range(m):
            print(arr[i][j] , end="")
        print("")
