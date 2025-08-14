



for t in range(1, int(input())+1):
    result = 0
    n = int(input())
    
    def resum(total):
        global result
        if total == n:
            result += 1
            return
        if total > n:
            return
        for i in range(1,4):
            resum(total + i)

    resum(0)
    print(result)
