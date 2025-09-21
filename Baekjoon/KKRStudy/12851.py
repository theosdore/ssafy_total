import sys
sys.stdin = open("C:\\Programming\\SSAFY_TOTAL\\Baekjoon\\KKRStudy\\input.txt")
from collections import deque

N, K = map(int,input().split())
# 한단계씩 나아가다가
# 찾으면 그 단계에 있는건 다 실행하고 갯수 새기
# 내가 들린 위치에오면 멈추기

que = deque()
que.append((N,0))
resultTime = 0
resultHow = 0
visited = [False]*(100000*2)
maxVisit = 100000*2 -1

while True:
    tempX, tempC = que.popleft()
    if tempX == K:
        resultTime = tempC
        resultHow += 1
        break
    add = tempX + 1
    sub = tempX - 1
    double = tempX*2
    
    if add <= maxVisit and not visited[add]:
        if add != K:
            visited[add] = True
        que.append((add, tempC + 1))
        
    if sub >= 0 and not visited[sub]:
        if sub != K:
            visited[sub] = True
        que.append((sub, tempC + 1))
        
    if double <= maxVisit and not visited[double]:
        if double != K:
            visited[double] = True
        que.append((double, tempC + 1))


while que:
    tempX, tempC = que.popleft()
    if tempC > resultTime:
        break
    if tempX == K and tempC == resultTime:
        resultHow += 1


print(resultTime)
print(resultHow)