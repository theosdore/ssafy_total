for t in range(int(input())):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    delta = [ (1,0), (0, 1), (-1, 0), (0, -1) ]
    delta_index = 0
    arr_x = 0
    arr_y = 0
    move_counter = n-1
    moved = 0
    move_twice = 0
    for i in range(1, n*n + 1):
        if i == 1:
            arr[arr_y][arr_x] = i
        elif i < n:
            arr_x += delta[delta_index][0]
            arr_y += delta[delta_index][1]
            arr[arr_y][arr_x] = i
        elif i == n:
            arr_x += delta[delta_index][0]
            arr_y += delta[delta_index][1]
            arr[arr_y][arr_x] = i
            delta_index = (delta_index + 1)%4
        else:
            arr_x += delta[delta_index][0]
            arr_y += delta[delta_index][1]
            arr[arr_y][arr_x] = i
            moved += 1
            if moved == move_counter:
                delta_index = (delta_index + 1) % 4
                move_twice += 1
                moved = 0
                if move_twice == 2:
                    move_twice = 0
                    move_counter -= 1

    print(f"#{t + 1}")
    for i in arr:
        print(*i)
