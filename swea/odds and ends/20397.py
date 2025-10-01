for t in range(1, int(input())+1):
    N, M = map(int,input().split())
    stoneLst = [0]+list(map(int, input().split()))
    changeOrder = tuple(tuple(map(int, input().split())) for _ in range(M))
    # 순서대로 뒤집기
    # 1부터 j번 째 돌까지 키워가며 범위 확인
    # 범위가 벗어나지 않으면 뒤집기
    for i in range(M):
        for j in range(1, changeOrder[i][1]+1):
            if 1 <= changeOrder[i][0] - j and changeOrder[i][0] + j <= N:
                if stoneLst[changeOrder[i][0] + j] == stoneLst[changeOrder[i][0] - j]:
                    if stoneLst[changeOrder[i][0] - j]:
                        stoneLst[changeOrder[i][0] + j] = stoneLst[changeOrder[i][0] - j] = 0
                    else:
                        stoneLst[changeOrder[i][0] + j] = stoneLst[changeOrder[i][0] - j] = 1

    print(f"#{t}",  *stoneLst[1:])

