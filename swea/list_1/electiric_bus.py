for t in range(int(input())):
    k, n, m = map(int, input().split())
    station_pos_list = list(map(int, input().split()))
    cnt = 0
    # 정류장 거리 리스트 생성
    distance_list = [station_pos_list[i] - station_pos_list[i-1] for i in range(1, len(station_pos_list))]
    # 각 옆칸을 더해서 최대한 긴 거리로 만듬





    """
    두가지 방향성
    - 정류장들의 거리를 확인 후 k보다 큰 값이 있으면 return 0
    - 거리를 합하다 k 보다 커지면 멈추고 리턴
    k < 정류장[0] -> k < 정류장[1]
    정류장[0] + k  < 정류장[2]
    - 0부터 k를 더해가면서 확인 
    
    
    """