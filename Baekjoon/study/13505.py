import sys
sys.stdin = open('C:\Aiden\ssafy_total\Baekjoon\study\input.txt')

# 문제의 입력값 N을 받음
N = int(input())
# N개의 정수를 리스트로 받음
numbers = list(map(int, input().split()))

# 트라이 자료구조를 표현할 딕셔너리. {0: {다음 노드}, 1: {다음 노드}} 형태로 구성됨
trie = {}

# 최종 결과를 저장할 변수
max_xor = 0

# 리스트의 각 숫자에 대해 반복
for num in numbers:
    # 1. 현재 숫자를 트라이에 삽입하는 과정
    
    # 루트 노드에서 시작
    node = trie
    # 29번 비트(가장 중요한 비트, MSB)부터 0번 비트(가장 덜 중요한 비트, LSB)까지 확인
    # 입력 수의 최댓값이 10억이므로, 2^30 미만임 (30비트로 표현 가능)
    for i in range(29, -1, -1):
        # 현재 숫자의 i번째 비트가 0인지 1인지 확인
        bit = (num >> i) & 1
        
        # 해당 비트의 경로가 트라이에 없으면 새로운 노드(딕셔너리)를 생성
        if bit not in node:
            node[bit] = {}
        # 해당 비트의 경로를 따라 다음 노드로 이동
        node = node[bit]

    # 2. 현재 숫자와 가장 큰 XOR 값을 만들 수 있는 수를 트라이에서 찾는 과정
    
    # 트라이에 숫자가 하나만 있다면 비교 대상이 없으므로 건너뜀
    if len(trie) == 0:
        continue

    # 루트 노드에서 시작
    node = trie
    # 현재까지 만들어진 XOR 값을 저장할 변수
    current_xor = 0
    # 마찬가지로 29번 비트부터 0번 비트까지 확인
    for i in range(29, -1, -1):
        # 현재 숫자의 i번째 비트
        bit = (num >> i) & 1
        # XOR 결과를 최대로 만들기 위해 필요한 반대 비트
        opposite_bit = 1 - bit

        # 만약 트라이에 반대 비트 경로가 존재한다면,
        # 그 경로를 선택하는 것이 현재 비트에서 XOR 결과를 최대로 만드는 방법임
        if opposite_bit in node:
            # 결과값의 i번째 비트를 1로 만들어줌 (2^i 만큼 값을 더함)
            current_xor |= (1 << i)
            # 반대 비트 경로를 따라 다음 노드로 이동
            node = node[opposite_bit]
        else:
            # 반대 비트 경로가 없다면, 어쩔 수 없이 같은 비트 경로를 따라감
            # 이 경우 결과값의 i번째 비트는 0이 되므로 current_xor에 아무런 변화를 주지 않음
            node = node[bit]
            
    # 현재 숫자로 만들 수 있는 최대 XOR 값을 찾았으므로, 전체 최댓값과 비교하여 갱신
    max_xor = max(max_xor, current_xor)

# 최종 결과 출력
print(max_xor)




































