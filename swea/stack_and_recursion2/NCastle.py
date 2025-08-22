# 그냥 팩토리얼로 풀기
# for t in range(1, 10):
#     N = int(input())
#     result = 1
#     for i in range(N, 0, -1):
#         result *= i
#     print(f"#{t} {result}")

# 재귀로 풀기
for t in range(1, 10):
    N = int(input())
    visited = [False]*N
    result = 0
    def recur(a):
        if a == N:
            global result
            result += 1
            return
        for i in range(N):
            if visited[i] == False:
                visited[i]  = True
                recur(a + 1)
                visited[i] = False
    recur(0)
    print(f"#{t} {result}")