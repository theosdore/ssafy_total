# find 함수: 특정 원소의 루트 노드를 찾는 함수 (경로 압축 적용)
def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

# union 함수: 두 원소가 속한 집합을 합치는 함수 (Union by Size 적용)
def union(parent, size, a, b):
    # 각 원소의 루트 노드를 찾음
    root_a = find(parent, a)
    root_b = find(parent, b)

    # 루트가 다를 경우에만 합치기 수행
    if root_a != root_b:
        # 크기가 작은 트리를 큰 트리에 붙인다
        if size[root_a] < size[root_b]:
            parent[root_a] = root_b
            size[root_b] += size[root_a] # 새로운 루트의 크기 갱신
        else:
            parent[root_b] = root_a
            size[root_a] += size[root_b] # 새로운 루트의 크기 갱신
    
    # ★★★ 두 사람이 속한 네트워크의 총 인원수는 합쳐진 후의 루트 노드의 size 값이다. ★★★
    return size[find(parent, a)]


# 메인 로직
# 테스트 케이스의 수
T = int(input())

for _ in range(T):
    # 친구 관계의 수
    F = int(input())

    # 각 테스트 케이스마다 자료구조 초기화
    parent = {}
    size = {}
    
    for _ in range(F):
        name1, name2 = input().split()

        # 이름(문자열)을 정수 ID로 매핑
        # 만약 이름이 처음 나온 것이라면, parent와 size 딕셔너리에 추가
        if name1 not in parent:
            parent[name1] = name1
            size[name1] = 1
        if name2 not in parent:
            parent[name2] = name2
            size[name2] = 1

        # union 연산을 수행하고, 합쳐진 네트워크의 크기를 출력
        network_size = union(parent, size, name1, name2)
        print(network_size)