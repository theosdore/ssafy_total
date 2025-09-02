for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    nodeSet = [tuple(map(int, input().split())) for _ in range(E)]
    firstN = set(nodeSet[0] for _ in range(E))
    S, G = map(int, input().split())
    