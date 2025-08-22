import sys
sys.stdin = open("swea\\stack_and_recursion2\\input.txt")
for t in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] *N
    result = 101

    def recur(a, total):
        global result
        if a == N:
            if total < result:
                result = total
            return
        
        if total >= result:
            return
        
        # 인덱스를 돌아가면서 
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                recur(a+1, total + arr[a][i])
                visited[i] = False

    recur(0, 0)

    print(f"#{t} {result}")