import sys
sys.stdin = open('input.txt')

def recur(nodeN):
    global N
    global result
    if nodeN > N:
        return
    if branch[nodeN][0] != 0:
        recur(branch[nodeN][0])
    result = result + tree[nodeN]
    if branch[nodeN][1] != 0:
        recur(branch[nodeN][1])


for t in range(1, 11):
    N = int(input())
    tree = [0]*(N+1)
    branch = [[0,0] for _ in range(N+1)]
    result = ""
    for _ in range(N):
        nodeInfo = input().split()
        nodeNum = int(nodeInfo[0])
        tree[nodeNum] = nodeInfo[1]
        if len(nodeInfo) == 3:
            branch[nodeNum][0] = int(nodeInfo[2])
        if len(nodeInfo) == 4:
            branch[nodeNum] = [int(nodeInfo[2]),int(nodeInfo[3])]
    recur(1)
    print(f"#{t} {result}")