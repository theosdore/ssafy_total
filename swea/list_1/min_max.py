
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cnt = int(input())
    if cnt == 0:
        input()
        continue
    lst = list(map(int, input().split()))
    print(f"리스트 {lst}")
    mini, maxi = lst[0], lst[0]
    print(mini, maxi)
    for num in lst:
        if num < mini:
            mini = num
        elif num > maxi:
            maxi = num
    print(f"#{test_case} {maxi-mini}")