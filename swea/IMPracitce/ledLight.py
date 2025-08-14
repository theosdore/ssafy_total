for t in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    off_num = 0
    result = 0
    for i in range(len(arr)):
        button_num = i + 1
        if arr[i] == 1:
            while button_num < n+1:
                arr[button_num-1] = 1 - arr[button_num-1]
                button_num += i + 1
            result += 1
    
    print(f"#{t} {result}")
