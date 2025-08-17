import sys
sys.stdin = open("sample_input.txt")

for t in range(1, int(input())+1):
    # sample길이 N, passcode길이 K
    N, K = map(int, input().split())
    #sample
    n_lst = list(map(int, input().split()))
    k_lst = list(map(int, input().split()))
    idx = 0
    for n in n_lst:
        if n == k_lst[idx]:
            idx += 1
            if idx == K:
                print(f"#{t} 1")
                break
    else:
        print(f"#{t} 0")
    
    