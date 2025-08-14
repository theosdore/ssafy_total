import sys
sys.stdin = open("input.txt")

for t in range(1, int(input()) + 1):
    result = []
    used_node = []

    def finding(i):
        global result
        result.append(i)
        used_node.append(i)
        for j in range(N):
            if arr[i][j] == 1 and j not in used_node:
                finding(j)

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    finding(0)

    print(f"#{t}", end=" ")
    print(*result)

    # arr[0] 탐색     for j in range(N): arr[0][j]
    # 1이 나오는 index 확인       if arr[0][j] == 1:
    # 인덱스 추출 -> 인덱스에 해당하는 행을 찾아서           arr[j][j']
    # 1이 나오는~ 반복
