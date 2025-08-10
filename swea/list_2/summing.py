for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    maxi_r = max(sum(x) for x in arr)
    maxi_c = max(sum(arr[j][i] for j in range(100)) for i in range(100))
    maxi_cross_1 = sum(arr[i][i] for i in range(100))
    maxi_cross_2 = sum(arr[i][99 - i] for i in range(100))

    print(f"#{t} {max(maxi_r, maxi_c, maxi_cross_2, maxi_cross_1)}")

    # maxi_c = max([max([arr[j][i] for j in range(9)]) for i in range(9)])
    # for i in range(9):
    #     temp_max = max([arr[j][i] for j in range(9)])
    #     if maxi_c < temp_max:
    #         maxi_c = temp_max

