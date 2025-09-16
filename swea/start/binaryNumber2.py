import sys
sys.stdin = open('input.txt')

for t in range(1, int(input()) + 1):
    N = float(input())
    cnt = 1
    result = ""
    while N > 0:
        if cnt == 13:
            result = "overflow"
            break
        if N >= 2**(-cnt):
            N -= 2**(-cnt)
            cnt += 1
            result = result + "1"
        else:
            cnt += 1
            result = result + "0"

    print(f"#{t} {result}")