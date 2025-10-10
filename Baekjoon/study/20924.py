import sys
sys.setrecursionlimit(10**6)

N, R = map(int,input().split())
branchMap = [[] for _ in range(N+1)]

def recurG(nodeN, length):
    global resultG
    global giganode
    if len(branchMap[nodeN]) > 2:
        return 
    for nextNode, templength in branchMap[nodeN]:
        if not visited[nextNode]:
            visited[nextNode] = True
            giganode = nextNode
            resultG = length + templength
            recurG(nextNode, length + templength)


def recurL(nodeN, length):
    global resultE
    if len(branchMap[nodeN]) <= 1:
        if resultE < length:
            resultE = length
        return 
    for nextNode, templength in branchMap[nodeN]:
        if not visited[nextNode]:
            visited[nextNode] = True
            recurL(nextNode, length + templength )


for _ in range(N-1):
    a,b,d = map(int, input().split())
    branchMap[a].append((b,d))
    branchMap[b].append((a,d))

visited = [False for _ in range(N+1)]
visited[R] = True
giganode = R
resultG = 0
resultE = 0
recurG(R, 0)
recurL(giganode, 0)
print(resultG, resultE)