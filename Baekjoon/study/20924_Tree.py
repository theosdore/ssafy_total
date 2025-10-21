import sys
# sys.stdin = open('ssafy_total\Baekjoon\study\input.txt')
input = sys.stdin.readline

N, R = map(int,input().split())
# 인접행렬 만들기
# 기둥 먼저 찾고 가지찾기 나눠야하나?
# 이미 지나간 노드는 안가도록
# 길이를 저장하면서 스택에 저장해야할거 같네

treemap = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, d = map(int,input().split())
    treemap[a].append((b,d)) 
    treemap[b].append((a,d))

#기가노드찾기 : 기준은 지나온거 빼고 두개이상일 때?
gigaStack = [(0, R, 0)]
gigaCounter = 0
result =[0, 0]
while gigaStack:
    parentN, currentN, distance = gigaStack.pop()
    gigaCounter = 0
    # 트리맵에 저장되어있는 연결된 브랜치를 스택에 추가. 단 부모 노드 추가 안되도록 할 것.
    for checkingN in treemap[currentN]:
        if checkingN[0] != parentN:
            gigaStack.append((currentN ,checkingN[0], distance + checkingN[1]))
            gigaCounter += 1
    
    result[0] = distance
    if gigaCounter > 1:
        break

if gigaStack:
    while gigaStack:
        parentN, currentN, distance = gigaStack.pop()
        for checkingN in treemap[currentN]:
            if checkingN[0] != parentN:
                gigaStack.append((currentN, checkingN[0], distance + checkingN[1]))
        if distance > result[1]:
            result[1] = distance
    print(result[0], result[1]- result[0])
else:
    print(result[0], 0)