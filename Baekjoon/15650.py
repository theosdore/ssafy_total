# N, M = map(int,input().split())

# path = []
# visited = [True]*(N+1)
# def recur(cnt):
#     if cnt == M:
#         print(*path)
#         return
#     for i in range(1, N+1): 
#         if visited[i]:
#             for j in range(1, i+1):
#                 visited[j] = False
#             path.append(i)
#             recur(cnt+1)
#             path.pop()
#             for j in range(1, i+1):
#                 visited[j] = True
# recur(0)

N, M = map(int, input().split())

# 중복 없는 순열 == 중복순열을 구현한 후에 중복을 제거
path = []


# prev: 이전에 선택한 값
def recur(cnt, prev):
    if cnt == M:
        print(*path)
        return

    # 재귀 호출 코드
    # - 이전에 선택한 값 다음부터 고려하면 된다
    for num in range(prev + 1, N + 1):
        path.append(num)  # num 추가
        recur(cnt + 1, num)
        path.pop()        # num 제거


recur(0, 0)