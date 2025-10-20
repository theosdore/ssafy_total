# 1번 도시에서 출발
# 1번에서 갈 수 있는 도시 쭉 리스트에 넣고
# 그 다음 쪽에서 갈 수 있는 도시 쭉 리스트에 넣기
# 도시 거리 저장해놓은 리스트 따로 만들기. 거기 보다 작으면 넣고 크면 버리기
# 근데 그럼 계속 작아지는건 어떻게 계산하지
# 음 그럼 인접 행렬 만들어서, 행렬도 같이 저장하다가, 더 작아지면 -1로 출력해야하나
import sys
sys.stdin = open('ssafy_total\Baekjoon\study\input.txt')

N, M = map(int,input().split())
busroutelst = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    A, B, C = map(int,input().split())
    busroutelst[A][B] = C

maplst = [float('inf')]*(N+1)
maplst[1] = 0
