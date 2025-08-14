import sys
sys.stdin = open("sample_input.txt")
for t in range(1, int(input())+1):
    view1 = [*map(int, input().split())]
    view2 = [*map(int, input().split())]

    # 1번 : 겹칠 때
    # 각 x좌표 y좌표 값들이 서로 범위 안에 있는지 확인
    if (view2[0] < view1[0] < view2[2] and view2[1] < view1[1] < view2[3]) or (view1[0] > view2[0] and view1[1] > view2[1]):

    # 2번 : 겹치는 선
    #