def recur(x):
    global tempH
    global B
    global minimumH
    global prev
    if B <= tempH :
        if tempH < minimumH:
            minimumH = tempH
        return
    for i in range(prev, N):
        tempH += heightLst[i]
        prev = i + 1
        recur(i)
        tempH -= heightLst[i]


for t in range(1, int(input())+1):
    N, B = map(int, input().split())
    heightLst = list(map(int, input().split()))
    heightLst.sort()
    minimumH = sum(heightLst)
    prev = 0
    tempH = 0
    visited = [False]*N
    recur(0)
    print(f"#{t} {minimumH - B}")

