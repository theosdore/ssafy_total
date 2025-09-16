import sys
sys.stdin = open('input.txt')

for t in range(1, int(input())+1):
    E, N = map(int,input().split())
    lines = tuple(map(int, input().split()))
    left = [0]*(E+2)
    right = [0]*(E+2)
    for i in range(0, E*2, 2):
        if left[lines[i]] == 0:
            left[lines[i]] = lines[i+1]
        else:
            right[lines[i]] = lines[i+1]

    # que = deque([N])
    stack = [N]
    result = 0
    while stack:
        tempN = stack.pop()
        if left[tempN] != 0:
            stack.append(left[tempN])
            result += 1
        if right[tempN] != 0:
            stack.append(right[tempN])
            result += 1

    print(f"#{t} {result+1}")
