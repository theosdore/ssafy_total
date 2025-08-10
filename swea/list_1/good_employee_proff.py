T = int(input())

for tc in range(1, T + 1):
    H, W = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(H)]

    dat = [0] * 10000001

    max_count = 0
    max_index = 0

    for i in range(H):
        for j in range(W):
            number = table[i][j]
            dat[number] += 1

            if max_count < dat[number]:
                max_count = dat[number]

    # max_count 가 2개 이상일 때,
    # max_index 는 한 번에 구할 수 없으니
    # 아래처럼 한 번 더 반복시켜 주어야 한다.
    for i in range(10000001):
        if dat[i] == max_count:
            max_index = i
            break

    print(f'#{tc} {max_index}')