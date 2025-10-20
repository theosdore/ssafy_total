N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# 비활성 바이러스 중에 M개를 바꿔서 계산해보기 -> 조합
# 모든 경우에 수에 대해? -> BFS
# 
