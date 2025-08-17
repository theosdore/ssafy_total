for t in range(1, int(input())+1):
    N, P = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dlts = [(0,1), (0,-1), (1,0), (-1,0)]
    maxi = 0
    for i in range(N):
        for j in range(N):
            temp_sum = arr[i][j]
            for dlt in dlts:
                for p in range(1, P+1):
                    dlx = i+dlt[0]*p
                    dly = j+dlt[1]*p
                    if dlx < 0 or dlx == N or dly < 0  or dly == N:
                        break
                    else:
                        temp_sum += arr[dlx][dly]
            if temp_sum > maxi:
                maxi = temp_sum

    print(f"#{t} {maxi}")