for t in range(1, int(input()) + 1):
    N = int(input())
    result = 0


    def collatz(x):
        global result
        if x == 1:
            return
        elif x % 2 == 1:
            result += 1
            return collatz(x * 3 + 1)
        else:
            result += 1
            return collatz(x // 2)

    collatz(N)
    print(f"#{t} {result}")