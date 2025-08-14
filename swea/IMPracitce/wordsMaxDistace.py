# import sys
# sys.stdin = open("sample_input.txt")
for t in range(1, int(input()) + 1):
    width = int(input())
    lst = list(input())
    arr = []
    result = 0
    for i in range(len(lst)):
        if lst[i] == "A":
            arr.append(i)
    length = len(arr)

    if length < width:
        print(f"#{t} {result}")
    elif length == width:
        print(f"#{t} {arr[-1] - arr[0]}")
    else:
        for i in range(length - width + 1):
            temp_res = arr[i + width - 1] - arr[i]
            if result < temp_res:
                result = temp_res
        print(f"#{t} {result}")
