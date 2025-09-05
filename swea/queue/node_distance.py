from collections import deque
for t in range(1, int(input())+1):
    V, E = map(int, input().split())
    Arrowlst = [[] for _ in range(V+1)]
    distaceLst = [0]*(V+1)
    visitLst = [True]*(V+1)
    for _ in range(E):
        tempA, tempB = map(int, input().split())
        Arrowlst[tempA].append(tempB)
        Arrowlst[tempB].append(tempA)
    S, G = map(int, input().split())
    qq = deque()
    qq.append(S)
    visitLst[S] = False
    while True:
        tempStep = qq.popleft()
        tempDistance = distaceLst[tempStep]
        if tempStep == G:
            print(f"#{t} {tempDistance}")
            break

        for nextStep in Arrowlst[tempStep]:
            if visitLst[nextStep]:
                qq.append(nextStep)
                distaceLst[nextStep] = tempDistance + 1
                visitLst[nextStep] = False

        if not qq:
            print(f"#{t} {0}")
            break






