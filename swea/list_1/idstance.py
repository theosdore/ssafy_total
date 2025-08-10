case = int(input())
for t in range(case):
    size = int(input())
    lst = list(map(int, input().split()))

    mini_pos = 0
    maxi_pos = size
    mini = 11
    maxi = 0

    for i in range(size):
        if lst[i] < mini:
            mini = lst[i]
            mini_pos = i
        if lst[i] >= maxi:
            maxi = lst[i]
            maxi_pos = i
    result = maxi_pos-mini_pos
    print(f"#{t+1} {result if result > 0 else -result}")
