import sys
sys.stdin = open('input.txt')
def heappush(nodeN):
    if tree[nodeN] < tree[nodeN//2] and nodeN//2 != 0:
        tree[nodeN], tree[nodeN // 2] = tree[nodeN//2],  tree[nodeN]
        return heappush(nodeN//2)
    return

for t in range(1, int(input())+1):
    N = int(input())
    nodelst = tuple(map(int, input().split()))
    tree = [0]
    for i in range(N):
        tree.append(nodelst[i])
        heappush(len(tree)-1)

    result = 0
    nodeN = (len(tree)-1)//2
    while True:
        if nodeN == 0:
            break
        result += tree[nodeN]
        nodeN = nodeN//2
    print(f"#{t} {result}")