import sys

sys.stdin = open('input.txt')


def recur(nodeNum):
    global N
    global cnt
    if nodeNum > N:
        return
    recur(nodeNum * 2)
    tree[nodeNum] = cnt
    cnt += 1
    recur(nodeNum * 2 + 1)


for t in range(1, int(input()) + 1):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1
    recur(1)
    print(f"#{t} {tree[1]} {tree[N // 2]}")
