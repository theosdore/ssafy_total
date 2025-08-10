
T = int(input())
for t in range(T):
    height_a, width_a = list(map(int, input().split()))
    apartment = []
    blacklists = [0] * 100001
    blacklist_count = 0
    for hc in range(height_a):
        apartment.append(list(map(int, input().split())))

    height_b, width_b = list(map(int, input().split()))

    for hb in range(height_b):
        temp_list = list(map(int, input().split()))
        for wb in range(width_b):
            blacklists[temp_list[wb]] += 1
    for h in range(height_a):
        for w in range(width_a):
            if blacklists[apartment[h][w]] != 0:
                blacklist_count += 1
    print(f'#{t + 1} {blacklist_count} {height_a * width_a - blacklist_count}')