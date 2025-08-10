#테스트케이스
for t in range(int(input())):
    #Ai, Bi 를 N개만큼 줌
    station_info = [0]*5000
    for _ in range(int(input())):
        a, b = map(int, input().split())
        for j in range(a-1, b):
            station_info[j] += 1
    #P만큼 j번째 줄에 정수가 주어짐
    result = [0]*int(input())
    for i in range(len(result)):
        result[i] = station_info[int(input())-1]
    print(f"#{t+1}", *result)