from collections import deque

N, K = map(int,input().split())

# 모든 이동 방법의 시간이 같음 -> bfs
# 한단계씩 확인, 이미 지나온 자리는 que에 넣지 않기
# 시간만 확인하면 되니까 각 큐에 있는 곳에 위치랑 시간 정보 저장
# 도착하면, 그 시간까지 찾기

que = deque()
que.append((N,0))
visited = [float('inf')]*200000
visited[N] = 0
resultT = 0
resultR = 0
while True:
    tempPos, tempTime  = que.pop()
    if tempPos == K:
        resultT = tempTime
        resultR += 1
        break
    if tempPos*2 < 200000 and tempTime + 1 <= visited[tempPos*2] :
        que.appendleft((tempPos*2, tempTime+1))
        visited[tempPos*2] = tempTime + 1
    if tempPos+1 < 200000 and tempTime + 1 <= visited[tempPos+1]:
        que.appendleft((tempPos+1, tempTime+1))
        visited[tempPos+1] = tempTime + 1
    if tempPos-1 >= 0 and tempTime + 1 <= visited[tempPos-1]:
        que.appendleft((tempPos-1, tempTime+1))
        visited[tempPos-1] = tempTime + 1

while que:
    tempPos, tempTime = que.pop()
    if tempTime > resultT:
        break
    if tempPos == K:
        resultR += 1

print(resultT)
print(resultR)