import sys
sys.stdin = open("input.txt")

for t in range(1, int(input())+1):
    N, Q = map(int, input().split())
    strengthLst = list(map(int,  input().split()))
    strengthLst.sort()
    resultlst = [0]*Q
    for _ in range(Q):
        targetsmall, targetbig = map(int, input().split())
        maxidx = len(strengthLst)-1
        left, right = 0, maxidx
        result = 0
        while True:
            mid = (left + right) // 2
            if right < left or right < 0 or left > maxidx:
                result -= left
                break
            if strengthLst[mid] >= targetsmall:
                right = mid -1
            else:
                left = mid + 1

        left, right = 0, maxidx
        while True:
            mid = (left + right) // 2
            if left > right or left > maxidx or right < 0:
                result += right
                break
            if strengthLst[mid] > targetbig:
                right = mid - 1
            else:
                left = mid + 1
        resultlst[_] = result+1

    print(f"#{t}", end = " ")
    print(*resultlst)
        # 가운데 확인해서 targetsmall보다 같거나 크면
        # 먼저 왼쪽으로 이동해서 targetsmall 끝부분 찾기
        # targetsmall보다 작으면 오른쪽으로 이동해서 찾기
        # 그다음 오른쪽으로 이동해서 targetbig 찾기