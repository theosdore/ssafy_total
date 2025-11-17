"""

# N : 수의 갯수     M : 수의 변경 횟수      K : 구간의 합 구하는 횟수
N, M, K = map(int, input().split())
numlst = [ int(input()) for _ in range(N)]
for _ in range(M+K):
    # a==1 -> b를 c로 변경  a==2 -> b부터 c까지 합함
    a, b, c = map(int, input().split())
    
    # a확인
    # a==1이면 변경
    if a ==1:
        numlst[b-1] = c
    # a==2이면 합해서 출력
    else:
        print(sum(numlst[b-1:c]))

"""

"""----------------------------------"""
"""N, M, K = map(int, input().split())
tempsum = 0
numsumlst = [0]*(N+1)
changelst = []
for i in range(N):
    tempsum += int(input()) 
    numsumlst[i+1] = tempsum
for _ in range(M+K):
    # a==1 -> b를 c로 변경  a==2 -> b부터 c까지 합함
    a, b, c = map(int, input().split())
    
    # a확인 후 특정 값 변경
    # b가 변경되어있으면 연쇄변경 후 계산
    if a==1:
        changelst.append((b,c))
    else:
        while changelst:
            
"""

"""------------------------------------"""

import sys
input = sys.stdin.readline

# 세그먼트 트리 만들기
"""
             1
        2          3
    4    5     6      7
   8 9 10 11 12 13 14  15
"""
# node 트리의 노드 번호, start ~ end 내가 채워야 할 노드의 갯수
def init(node, start, end):
    # 노드의 범위가 하나라면, 즉 하나의 칸만 된다면
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end)//2
    # 재귀
    tree[node]= init(node*2, start, mid) + init(node*2+1, mid + 1, end)
    return tree[node]


def update(node, start, end, diff, index):
    if index < start or index > end:
        return
    tree[node] += diff
    if start != end:
        mid = (start + end)//2
        update(node*2, start, mid, diff, index)
        update(node*2+1, mid + 1, end, diff, index)

def query(node, start, end, leftidx, rightidx):
    if leftidx > end or rightidx < start:
        return 0
    if start >= leftidx and rightidx >= end:
        return tree[node]
    
    mid = (start + end)//2
    return query(node*2, start, mid, leftidx, rightidx) + query(node*2+1, mid+1, end, leftidx, rightidx)

N, M, K = map(int, input().split())
arr = [0]+[int(input()) for _ in range(N)]
tree = [0]*1000001
init(1, 1, N)
for i in range(M+K):
    a,b,c = map(int,input().split())
    if a ==1:
        arr[b] = c
        update(1, 1, N, c - arr[b], b)
    else:
        print(query(1, 1, N, b, c))