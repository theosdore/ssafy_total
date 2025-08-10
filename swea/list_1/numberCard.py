for t in range(int(input())):
    num_of_cards = int(input())
    lst = [0]*10
    cards = list(input())
    maxi = 0
    maxi_num = 0
    for card in cards:
        card = int(card)
        lst[card] += 1
        if lst[card] > maxi :
            maxi = lst[card]
            maxi_num = card
        elif lst[card] == maxi and card > maxi_num:
            maxi = lst[card]
            maxi_num = card

    print(f"#{t+1} {maxi_num} {maxi}")