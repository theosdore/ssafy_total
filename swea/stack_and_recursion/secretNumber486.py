import sys
sys.stdin = open("input.txt")
for t in range(1, 11):
    n, test_case =  input().split()
    test_case = list(test_case)
    result = []
    for i in range(len(test_case)):
        if len(result) == 0:
            result.append(test_case[i])
        elif result[-1] == test_case[i]:
            result.pop()
        else:
            result.append(test_case[i])
    print(f"#{t} {''.join(result)}")
