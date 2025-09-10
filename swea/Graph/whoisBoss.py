for t in range(1, int(input())+1):
    n = int(input())
    arr =[list(map(int,input().split())) for _ in range(n)]
    def findBoss():
        for i in range(n):
            if arr[i][0] == 1:
                print(f"#{t} boss:{i}", end = " ")
                return
    findBoss()
    underlst = [i for i in range(n) if arr[0][i] ==1]
    print(f"/ under:", end="")
    print(*underlst)
