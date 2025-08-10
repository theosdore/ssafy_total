def devideTillEnd(N, deviding_num):
    """
    n을 a로 나눔
    나눠서 몫이 0이거나 나머지가 나오면 멈춤
    1을 리턴
    반복 : 1과 자기 함수의 1을 더해서 리턴
    """
    remain = N%deviding_num
    share = N//deviding_num
    
    if remain == 0:
        return devideTillEnd(share, deviding_num) + 1
    else: 
        return 0


for t in range(int(input())):
    lst = [ 11, 7, 5, 3, 2]
    result = [0]*5
    N = int(input())
    for i in range(len(lst)):
        result[len(lst) - 1 - i] = devideTillEnd(N, lst[i])
    print(f"#{t+1}",*result)




# for t in range(int(input())):
#     lst = [ 11, 7, 5, 3, 2]
#     result = [0]*5
#     num = int(input())
#     for i in range(len(lst)):
#         while True:
#             if num%lst[i] != 0:
#                 break
#             num /= lst[i]
#             result[4-i] += 1
#     print(f"#{t+1} {result[0]} {result[1]} {result[2]} {result[3]} {result[4]}")