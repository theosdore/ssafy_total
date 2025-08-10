
for t in range(1, int(input())+1):
    lst = input()
    cnt_list = [0]*26
    for i in lst:
        cnt_list[ord(i)-97] += 1
    print(f"#{t}", *cnt_list)