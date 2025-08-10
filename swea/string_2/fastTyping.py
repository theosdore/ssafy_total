for t in range(1, int(input())+1 ):
    a, b = input().split()

    print(f"#{t} {len(a) - a.count(b)*(len(b)-1)}")