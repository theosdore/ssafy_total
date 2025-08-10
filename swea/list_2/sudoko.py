for t in range(1, int(input())+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1

    for i in range(9):
        if len(set(arr[i])) != 9 or len(set(arr[j][i] for j in range(9))) != 9:
            result = 0
            break

    if result == 1:
        for i in range(9, step=3):
            for j in range(9, step=3):
                temp_lst = [0]*9
                for k in range(3):
                    for l in range(3):
                        temp_lst[k*3+l] = arr[i+k][j+l]
                if len(set(temp_lst)) != 9:
                    result = 0
                    break

    print(f"#{t} {result}")