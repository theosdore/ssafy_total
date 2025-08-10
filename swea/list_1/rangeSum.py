# 테스트케이스 입력

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

# 숫자 개수, 범위 r 입력

    a, b = map(int, input().split())
# 인덱스 0 부터 n-1-(r-1) 까지 -> range
# for문으로 r범위 더해서 비교하기 반복 -> mini, maxi
    lst = list(map(int, input().split()))
    maxi = 0
    mini = 10000*b
    for i in range(a - b + 1):
        sum_temp = sum(lst[i:i+b])
        # print('썸템프', sum_temp)
        if sum_temp >= maxi:
            maxi = sum_temp
        if sum_temp <= mini:
            mini = sum_temp
    print(f"#{test_case} {maxi-mini}")
