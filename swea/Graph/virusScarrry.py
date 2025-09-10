# for t in range(1, int(input())+1):
#     n = int(input())
#     k = int(input())
#     lst = [tuple(map(int, input().split())) for _ in range(k)]
#     virused = set()
#     visited = [False]*k
#     result = 0
#     changed = True
#     while changed:
#         changed = False
#         for i in range(k):
#             if not visited[i]:
#                 if (lst[i][0] in virused) or (lst[i][1] in virused) or (1 in lst[i]):
#                     virused.add(lst[i][0])
#                     virused.add(lst[i][1])
#                     visited[i] = True
#                     changed = True
#
#     print(f"#{t} {len(virused)-1}")

    #인접행렬 인접리스트1
for t in range(1, int(input())+1):
    n = int(input())
    k = int(input())
    arr = [[] for _ in range(n+1)]
    for _ in range(k):
        a = list(map(int, input().split()))
        if a[1] not in arr[a[0]]:
            arr[a[0]].append(a[1])
        if a[0] not in arr[a[1]]:
            arr[a[1]].append(a[0])
    visited = [False]*(n+1)
    visited[1] = True
    def recur(x):
        for i in range(len(arr[x])):
            if not visited[arr[x][i]]:
                visited[arr[x][i]] = True
                recur(arr[x][i])
        return
    recur(1)
    result = 0
    for _ in visited:
        if _:
            result +=1
    print(f"#{t} {result-1}")
