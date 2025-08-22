for t in range(1, int(input())+1):
    N = int(input())
    main_tree = [[] for _ in range(N+1)]

    result=[[] for _ in range(3)]
    def dfs(node):
        if node == -1:
            return
        
        result[1].append(node)
        dfs(main_tree[node][0])
        result[0].append(node)
        dfs(main_tree[node][1])
        result[2].append(node)
        pass


    for _ in range(N):
        node, left, right = map(int, input().split())
        main_tree[node].append(left)
        main_tree[node].append(right)

    dfs(1)
    print(f"#{t}")
    print(*result[0])
    print(*result[1])
    print(*result[2])
