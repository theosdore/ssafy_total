import sys
sys.stdin = open('input.txt')


N , R = map(int, input().split())

branchs = [tuple(map(int, input().split())) for _ in range(N-1)]
branchlst = [[] for _ in range(N)]

for i in range(N-1):
    branchlst[branchs[i][0]].append((branchs[i][1], branchs[i][2]))
    branchlst[branchs[i][1]].append((branchs[i][0], branchs[i][2]))
print(branchlst)

cumulativeValue = [0]*(N+1)

stack = [R]
stack.append(R)
trunk = 0

#
# while stack:
#     tempN = stack.pop()
#     branchEA = 0
#     for i in range(len(branchlst)):
#         if cumulativeValue[branchlst[i][1]] == 0 and branchlst[i][0] == tempN:
#             if branchlst[i][1] != R:
#                 cumulativeValue[branchlst[i][1]] = cumulativeValue[branchlst[i][0]] + branchlst[i][2]
#                 stack.append(branchlst[i][1])
#                 branchEA += 1
#         if cumulativeValue[branchlst[i][0]] == 0 and branchlst[i][1] == tempN:
#             if branchlst[i][0] != R :
#                 cumulativeValue[branchlst[i][0]] = cumulativeValue[tempN] + branchlst[i][2]
#                 stack.append(branchlst[i][0])
#                 branchEA += 1
#     if branchEA >= 2 and trunk == 0:
#         trunk = tempN
# if trunk == 0:
#     print(max(cumulativeValue), 0)
# else:
#     print(cumulativeValue[trunk], max(cumulativeValue)-cumulativeValue[trunk])