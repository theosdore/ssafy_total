import sys
sys.stdin = open("input.txt")
for t in range(1, 11):
    number_of_roads = int(input().split()[1])*2
    arr = input().split()
    roads_set = [[] for _ in range(100)]
    for i in range(number_of_roads, step=2):
        roads_set[int(arr[i+1])].append(int(arr[i]))
    recall_stack = []
    index = 99
    result = 1
    while index != 0:
        if len(roads_set[index]) == 0:
            if len(recall_stack) == 0:
                result = 0
                break
            else:
                index = recall_stack.pop()
        else:
            for i in range(1, len(roads_set[index])):
                recall_stack.append(roads_set[index][i])
            index = roads_set[index][0]

    print(f"#{t} {result}")
