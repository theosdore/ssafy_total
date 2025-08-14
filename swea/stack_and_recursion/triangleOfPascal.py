for t in range(1, int(input())+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            if i+j == 0:
                arr[i][j] = 1
            elif j-1 < 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = sum(arr[i-1][j-1:j+1])

    print(f"#{t}")
    for lst in arr:
        for x in lst:
            if x != 0:
                print(x, end=" ")
        print()

