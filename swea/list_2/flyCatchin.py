for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    maxi = 0

    for i in range(n-m+1):
        for j in range(n-m+1):
            temp_sum = 0
            for k in range(m):
                for l in range(m):
                    temp_sum += arr[i+k][j+l]
            if maxi < temp_sum:
                maxi = temp_sum
    print(f"#{t} {maxi}")