def recur(nodeN):
    global cnt
    global n
    if nodeN > n:
        return
    
    recur(nodeN*2)
    tree[nodeN] = cnt
    cnt += 1
    recur(nodeN*2+1)


for t in range(1, int(input())+1):
    n = int(input())
    tree = [0]*(n+1)
    cnt = 1
    
    recur(1)
    print(f"#{t} {tree[1]} {tree[n//2]}")