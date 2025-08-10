""" 딕셔너리로 풀기

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    h, w = map(int, input().split())
    employee_dict = {}
    for i in range(h):
        key_nums = list(map(int, input().split()))
        for key_num in key_nums:
            if employee_dict.get(key_num):
                employee_dict[key_num] += 1
            else:
                employee_dict[key_num] = 1
    maxi_key = 0
    maxi = 0
    for key, cnt in employee_dict.items():
        if cnt > maxi:
            maxi = cnt
            maxi_key = key
        elif cnt == maxi and key < maxi_key:
            maxi_key = key
    print(f"#{test_case} {maxi_key}")

"""


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    h, w = map(int, input().split())
