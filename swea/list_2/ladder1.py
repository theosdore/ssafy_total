# # 매 번 입력 붙여넣기가 힘드니, 파일에서 입력을 받아오는 방식
# import sys
# sys.stdin = open("input.txt")

for _ in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 사다리 인덱스 모음
    ladder_index = [i for i in range(len(arr[0])) if arr[0][i] != 0]
    # 사다리 인덱스 모음의 인덱스
    goal_index = ladder_index.index(arr[99].index(2))
    # 올라가다 만나면 움직이고 또 올라가다 만나면 움직이고
    height = 0
    while height < 99:

        if ladder_index[goal_index] == 0:
            if arr[99-height][ladder_index[goal_index]+1] == 1:
                goal_index += 1
        elif ladder_index[goal_index] == 99:
            if arr[99-height][ladder_index[goal_index]-1] == 1:
                goal_index -= 1
        else:
            if arr[99-height][ladder_index[goal_index]+1] == 1:
                goal_index += 1
            elif arr[99-height][ladder_index[goal_index]-1] == 1:
                goal_index -= 1
        height += 1


    print(f"#{t} {ladder_index[goal_index]}")