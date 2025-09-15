import sys
sys.stdin = open('C:/Programming/SSAFY_TOTAL/Baekjoon/unionFInd/input.txt')
n, m = map(int, input().split())

originTree = [i for i in range(n+1)]
treeSize = [1]*(n+1)

def union(a, b):
    ancA = findParent(a)
    ancB = findParent(b)
    
    if ancA == ancB:
        return
    else:
        if treeSize[ancA] >= treeSize[ancB]:
            treeSize[ancA] += treeSize[ancB]
            originTree[ancB] = ancA
        else:
            treeSize[ancB] += treeSize[ancA]
            originTree[ancA] = ancB
        
def find(a,b):
    ancA = findParent(a)
    ancB = findParent(b)
    
    if ancA == ancB:
        print("YES")
    else:
        print("NO")
    
def findParent(x):
    if x != originTree[x]:
        originTree[x]= findParent(originTree[x])
        return originTree[x]
    else:
        return x
        

for _ in range(m):
    f, a, b = map(int, input().split())
    if f ==0:
        union(a, b)
    elif f==1:
        find(a, b)