for t in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    p = int(input())
    delta = [0]*(n+1)
    for _ in range(p):
        start, end, cost = map(int, input().split())
        delta[start] += cost
        delta[end+1] -= cost

    current_delta = 0
    for i in range(n):
        current_delta += delta[i]
        lst[i] += current_delta
    print(f"#{t+1}", *lst)
