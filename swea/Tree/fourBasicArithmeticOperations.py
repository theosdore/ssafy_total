import sys
sys.stdin = open('input.txt')
def recur(nodeN):
    # 왼쪽으로 타고 내려감 branchinfo확인해서 자식 없으면 부모 노드와 연산
    # 왼쪽 확인 후 연산자 확인 후 오른쪽 확인 하면서 반

    if LeftbranchInfo[nodeN] != 0:
        leftV = recur(LeftbranchInfo[nodeN])
    if RightbranchInfo[nodeN] != 0:
        rightV = recur(RightbranchInfo[nodeN])
    if tree[nodeN] == "-":
        return leftV - rightV
    elif tree[nodeN] == "+":
        return leftV + rightV
    elif tree[nodeN] == "*":
        return leftV*rightV
    elif tree[nodeN] == "/":
        return leftV/rightV
    else:
        return tree[nodeN]



for t in range(1, 11):
    N = int(input())
    tree = [0]*(N+1)
    LeftbranchInfo = [0]*(N+1)
    RightbranchInfo = [0] * (N + 1)
    for _ in range(N):
        whatIget = input().split()
        if len(whatIget) == 2:
            tree[int(whatIget[0])] = int(whatIget[1])
        else:
            nodeN = int(whatIget[0])
            tree[nodeN] = whatIget[1]
            LeftbranchInfo[nodeN] = int(whatIget[2])
            RightbranchInfo[nodeN] = int(whatIget[3])

    print(f"#{t}", int(recur(1)))