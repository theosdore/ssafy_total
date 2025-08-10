# b를 d로 이렇게 글자 거울모드 시키고
# 그리고 거꾸로 재생

for t in range(1, int(input())+1):
    words = input().translate(str.maketrans("qpbd","pqdb"))
    print(f"#{t}",words[::-1])

