# v : 정점 개수  e : 간선 개수
v, e = map(int, input().split())
# k : 시작 정점 번호
k = int(input())
# 간선 정보 u,v,w
arr = [ tuple(map(int, input().split())) for _ in range(e)]

