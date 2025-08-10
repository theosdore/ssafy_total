# for t in range(1, int(input())+1):
#     n, k = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     cnt = 0
#
#     for i in range(n):
#         temp_stack_r = 0
#         temp_stack_c = 0
#         for j in range(n):
#             if arr[i][j]:
#                 temp_stack_r += 1
#                 if j == n - 1 and temp_stack_r == k:
#                     cnt += 1
#             else:
#                 if temp_stack_r == k:
#                     cnt += 1
#                 temp_stack_r = 0
#
#             if arr[j][i]:
#                 temp_stack_c += 1
#                 if j == n - 1 and temp_stack_c == k:
#                     cnt += 1
#             else:
#                 if temp_stack_c == k:
#                     cnt += 1
#                 temp_stack_c = 0
#
#     print(f"#{t} {cnt}")
for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0

    print(f"#{t} {cnt}")