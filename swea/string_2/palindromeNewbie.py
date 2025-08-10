for t in range(1, int(input())+1 ):
    word = input().strip()
    result = 1
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            result = 0
            break
    print(f"#{t} {result}")