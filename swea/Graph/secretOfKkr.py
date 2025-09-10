from collections import deque

for t in range(1, int(input())+1):
    # currentNum , answerNum = map(lambda x : deque(map(int, list(x.zfill(4)))), input().split())
    currentNum, answerNum = map(lambda x: x.zfill(4), input().split())
    # 왔다갔다 안하기?
    que = deque()
    que.append((currentNum, ""))
    result = ""
    alreadycheckedset = set()
    if currentNum != answerNum:
        while True:
            tempQ = que.popleft()
            tempN = int(tempQ[0])
            # tempN -> DSLR 큐에 저장
            #double
            tempA = str((tempN*2)%10000).zfill(4)
            tempB = tempQ[1]+"D"
            if tempA == answerNum:
                result = tempB
                break
            if tempA not in alreadycheckedset:
                que.append((tempA, tempB))
                alreadycheckedset.add(tempA)
            #sub

            tempA = str(tempN -1 if tempN != 0 else 9999).zfill(4)
            tempB = tempQ[1] + "S"
            if tempA == answerNum:
                result = tempB
                break
            if tempA not in alreadycheckedset:
                que.append((tempA, tempB))
                alreadycheckedset.add(tempA)

            # left
            if len(tempQ[1])==0 or tempQ[1][-1] != "R":
                tempA = tempQ[0][1:] + tempQ[0][0]
                tempB = tempQ[1] + "L"
                if tempA == answerNum:
                    result = tempB
                    break
                if tempA not in alreadycheckedset:
                    que.append((tempA, tempB))
                    alreadycheckedset.add(tempA)
            #right
            if len(tempQ[1])==0 or tempQ[1][-1] != "L":
                tempA = tempQ[0][-1] + tempQ[0][:-1]
                tempB = tempQ[1] + "R"
                if tempA == answerNum:
                    result = tempB
                    break
                if tempA not in alreadycheckedset:
                    que.append((tempA, tempB))
                    alreadycheckedset.add(tempA)
    print(f"#{t}", result)
