case = int(input())
for t in range(case):
    input()
    lst = [len(i) for i in input().split("0")]
    print(f"#{t+1} {max(lst)}")