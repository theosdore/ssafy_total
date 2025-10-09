import sys
sys.stdin = open('ssafy_total\\Baekjoon\\KKR\\input.txt')

from collections import deque
N , R = map(int, input().split())

branchs = [tuple(map(int, input().split())) for _ in range(N-1)]
branchlst = [[] for _ in range(N+1)]

for i in range(N-1):
    branchlst[branchs[i][0]].append((branchs[i][0], branchs[i][1], branchs[i][2]))
    branchlst[branchs[i][1]].append((branchs[i][1], branchs[i][0], branchs[i][2]))

stack = deque()
stack.extend(branchlst[R])
visited = [0]*(N+1)
gigaN = 0
while stack:
    tempN = stack.popleft()
    if not visited[tempN[1]] and tempN[1] != R :
        stack.extend(branchlst[tempN[1]])
        visited[tempN[1]] = visited[tempN[0]] + tempN[2]
        if len(branchlst[tempN[1]]) >=3 and not gigaN:
            gigaN = visited[tempN[1]]
    
if len(branchlst[R]) >= 3:
    gigaN = 0

print(gigaN, max(visited) - gigaN )