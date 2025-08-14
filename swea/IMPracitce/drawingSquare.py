import sys

sys.stdin = open("sample_input.txt")
for t in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    counter = 0
    how_big = 0
    for i in range(N):
        for j in range(N):
            start_p = arr[i][j]
            for k in range(i, N):
                for l in range(j, N):
                    if arr[k][l] == start_p:
                        this_big = (k-i+1)*(l-j+1)
                        if this_big == how_big:
                            counter += 1
                        elif this_big > how_big:
                            how_big = this_big
                            counter = 1

    print(f"#{t} {counter}")

