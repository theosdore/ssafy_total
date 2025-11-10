# v : 정점 개수  e : 간선 개수
V, E = map(int, input().split())
# k : 시작 정점 번호
K = int(input())
# 인접 리스트
table = [[] for _ in range(E+1)]
# 간선 정보 u,v,w
for _ in range(E):
    u,v,w = map(int(input().split()))
    table[u].append((v,w))
