for t in range(1, int(input()) + 1):
    N = int(input())
    tree = [ [] for _ in range(N + 1)]
    for _ in range(N):
        idx, lftn, rgtn = map(int, input().split())
        tree[idx] = [lftn, rgtn]
    def pattern1(x):
        if tree[x][0] != -1:
            pattern1(tree[x][0])
        result.append(x)
        if tree[x][1] != -1:
            pattern1(tree[x][1])
    def pattern2(x):
        result.append(x)
        if tree[x][0] != -1:
            pattern2(tree[x][0])
        if tree[x][1] != -1:
            pattern2(tree[x][1])
    def pattern3(x):
        if tree[x][0] != -1:
            pattern3(tree[x][0])
        if tree[x][1] != -1:
            pattern3(tree[x][1])
        result.append(x)
    print(f"#{t}")
    result = []
    pattern1(1)
    print(*result)

    result = []
    pattern2(1)
    print(*result)

    result = []
    pattern3(1)
    print(*result)