# import sys
# sys.stdin = open("sample_input.txt")
for t in range(1, int(input())+1):
    ax1, ay1, ax2, ay2 = map(int, input().split())
    bx1, by1, bx2, by2 = map(int, input().split())
    # 4번 : 안겹치는 경우
    if (ax1 > bx2) or (bx1 > ax2) or (ay1 > by2) or (by1 > ay2):
        print(f"#{t} 4")
        continue
    # 3번 : 겹치는 점    
    # a 오른 b 왼 / a아래 b 위 / a 오른 b 왼
    elif (ax2 == bx1 and ay2 == by1) or (ax2==bx1 and ay1== by2) or (ax1 == bx2 and ay1 == by2) or (ax1 == bx2 and ay2 == by1):
        print(f"#{t} 3")
        continue
    # 2번 : 겹치는 선 
    elif (ax2 == bx1) or (ay2 == by1) or (ax1 == bx2) or (ay1 == by2):
        print(f"#{t} 2")
        continue
    else : 
        print(f"#{t} 1")
    



