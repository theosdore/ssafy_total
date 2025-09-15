import sys
sys.stdin = open("input.txt")


for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    mapmap = [[] for _ in range(N+1)]
    for _ in range(M):
        nodeA, nodeB = map(int, input().split())
        mapmap[nodeA].append(nodeB)
        mapmap[nodeB].append(nodeA)
    R, K = map(int, input().split())
    if K == 0:
        print(f"#{t} 1")
        continue
    stack = [(R, 0)]
    visitset = {R}
    while stack:
        tempNode, tempCnt = stack.pop()
        for i in mapmap[tempNode]:
            if i not in visitset:
                if (tempCnt + 1) == K:
                    visitset.add(i)
                    continue
                visitset.add(i)
                stack.append((i, tempCnt + 1))

    print(f"#{t} {len(visitset)}")