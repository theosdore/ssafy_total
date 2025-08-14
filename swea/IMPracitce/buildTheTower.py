# # 탑 두개를 구성하고 있는 블록들이 각각 다른 블록들로 구성
# # 탑을 쌓을 때 블럭의 개수가 종류별로 오름차순으로 쌓여야 함
# # 최소 비용을 구해라?????!??!?!?!

# for t in range(1, int(input())+1):
#     n, m1, m2 = map(int, input().split())
#     arr = list(map(int, input().split()))
#     result = 0
#     m1_floor = 1
#     m2_floor = 1
#     while len(arr) > 0:
#         temp_max = arr.pop(arr.index(max(arr)))
#         # 층이 안채워졌을 때
#         if m1_floor <= m1 and m2_floor <= m2:
#             if m1_floor <= m2_floor:
#                 result += m1_floor*temp_max
#                 m1_floor += 1
#             else:
#                 result += m2_floor*temp_max
#                 m2_floor += 1
#         # m1이 채워졌을 때
#         elif m1_floor > m1:
#             # m2에만 담기
#             result += m2_floor*temp_max
#             m2_floor += 1
#         # m2가 채워졌을 때
#         else:
#             result += m1_floor*temp_max
#             m1_floor += 1

#     print(f"#{t} {result}")


for t in range(1, int(input())+1):
    n, m1, m2 = map(int, input().split())
    kilo_list = sorted(list(map(int, input().split())), reverse=True)
    lst = sorted([x for x in range(1, m1 + 1)] + [x for x in range(1, m2+1)])
    print("#"+str(t), sum([kilo_list[i]*lst[i] for i in range(n)]))
