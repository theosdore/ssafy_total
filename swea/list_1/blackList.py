T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    h, w = map(int, input().split())
    lst = []
    for i in range(h):
        lst.append(map(int, input().split()))

    bh, bw = map(int, input().split())
    black_list = set()
    for i in range(bh):
        for j in input().split():
            black_list.add(int(j))
    blacks = 0
    for floor in lst:
        for room in floor:
            if room in black_list:
                blacks += 1

    print(f"#{test_case} {blacks} {h*w - blacks }")
