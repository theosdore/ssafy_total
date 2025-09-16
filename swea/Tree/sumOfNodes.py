import sys
sys.stdin = open('input.txt')
for t in range(1, int(input())+1):
    N, M, L = map(int,input().split())
    tree = [0]*(N+1)
    for _ in range(M):
        tempNode, tempValue = map(int,input().split())
        while tempNode != 0:
            tree[tempNode] += tempValue
            tempNode = tempNode//2
    print(f"#{t} {tree[L]}")
