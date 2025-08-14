N = int(input())
cards = [i for i in range(N, 0, -1)]


# 카드를 2개 빼고, 하나를 제일 앞에 삽입하는 과정을 반복
# -> 카드가 2개 이상 있어야 2번 pop 가능
while len(cards) >= 2:
    print(cards.pop(), end=' ')  # 제일 뒤에 걸 뽑아서 출력
    num = cards.pop()     # 제일 뒤에 걸 뽑는다
    # insert: 한 칸씩 뒤로 다 민다 (499,999 연산 발생)
    cards.insert(0, num)  # 제일 앞에 넣는다

# 남은 카드 하나를 출력
print(cards[0])