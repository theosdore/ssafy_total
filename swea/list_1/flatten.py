# for t in range(1, 11):
#     dump_cnt = int(input())
#     box_list = list(map(int, input().split()))
#     for _ in range(dump_cnt):
#         if max(box_list) - min(box_list) <= 1:
#             print("끝")
#             break
#         box_list[box_list.index(max(box_list))] -= 1
#         box_list[box_list.index(min(box_list))] += 1
#     print(f"#{t} {max(box_list) - min(box_list)}")
for t in range(1, 11):
    dump_cnt = int(input())
    box_list = sorted(list(map(int, input().split())))
    for _ in range(dump_cnt):
        if box_list[-1] - box_list[0] <= 1:
            break
        box_list[-1] -= 1
        box_list[0] += 1
        box_list.sort()
    print(f"#{t} {box_list[-1] - box_list[0]}")
