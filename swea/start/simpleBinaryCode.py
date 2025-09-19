import sys

sys.stdin = open('input.txt')
for t in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    code = ""
    checked = False
    for _ in range(N):
        tempcode = input()
        if not checked:
            if "1" in tempcode:
                code = tempcode
                checked = True
    endpoint = 0
    for j in range(M - 1, -1, -1):
        if code[j] == "1":
            endpoint = j
            break
    startpoint = endpoint - 55
    beforecode = code[startpoint]
    counter = 0
    resultC = 0
    result = [0, 0, 0, 0]
    decode = []
    for i in range(8):
        beforecode = code[startpoint + i*7]
        for j in range(7):
            currentcode = code[startpoint + i * 7 + j]
            if currentcode == beforecode:
                counter += 1
            else:
                result[resultC] = counter
                resultC += 1
                counter = 1
            beforecode = currentcode
        result[resultC] = counter
        resultC = 0
        counter = 0
        first = result[0]
        second = result[1]
        third = result[2]
        if first == 3:
            if second == 2:
                decode.append(0)
            else:
                decode.append(9)
        elif first == 2:
            if second == 1:
                decode.append(2)
            else:
                decode.append(1)
        else:
            if second == 2:
                if third == 3:
                    decode.append(5)
                else:
                    decode.append(8)
            elif second == 3:
                decode.append(7)
            elif second == 1:
                if third == 1:
                    decode.append(6)
                else:
                    decode.append(4)
            else:
                decode.append(3)

    odd = 0
    even = 0
    for i in range(0, 8, 2):
        odd += decode[i]
    for i in range(1, 8, 2):
        even += decode[i]
    finalR = odd * 3 + even
    if finalR % 10 == 0:
        print(f"#{t} {sum(decode)}")
    else:
        print(f"#{t} 0")
