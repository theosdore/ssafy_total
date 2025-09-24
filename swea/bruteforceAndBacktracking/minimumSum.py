import sys
# sys.stdin = open("C:\\Programming\\SSAFY_TOTAL\\swea\\bruteforceAndBacktracking\\input.txt")
sys.stdin = open("SSAFY_TOTAL\\swea\\bruteforceAndBacktracking\\input.txt")

def recur(a, b):
    global result
    global tempR
    if tempR >= result:
        return
    if a == N-1 and b == N -1:
        if tempR < result:
            result = tempR
        return
    
    if a + 1 < N:
        tempR += arr[a+1][b]
        recur(a+1, b)
        tempR -= arr[a+1][b]
    if b + 1< N:
        tempR += arr[a][b+1]
        recur(a, b+1)
        tempR -= arr[a][b+1]
    
    
for t in range(1, int(input())+1):
    N = int(input())
    result = 12*12*9 + 1
    arr = [ list(map(int, input().split())) for _ in range(N) ]
    tempR = arr[0][0]
    recur(0,0)
    print(f"#{t} {result}")