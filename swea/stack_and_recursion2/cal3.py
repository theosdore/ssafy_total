import sys
sys.stdin = open("swea\\stack_and_recursion2\\input.txt")
for t in range(1, 11):
    N = int(input())
    arr = list(input())
    result = []
    words_lst = []
    words_dic = {
        "*" : 2,
        "/" : 2,
        "+" : 1,
        "-" : 1,
    }
    for i in range(len(arr)):
        temp_a = arr[i]
        if temp_a.isnumeric():
            result.append(int(arr[i]))
        elif temp_a == ")":
            while True:
                temp_b = words_lst.pop()
                if temp_b == "(":
                    break
                result.append(temp_b)
        elif temp_a =="(":
            words_lst.append(temp_a)
        elif temp_a in words_dic:
            while (words_lst and words_lst[-1] != "(" and (words_dic[temp_a] < words_dic[words_lst[-1]])):
                result.append(words_lst.pop())
            words_lst.append(temp_a)
        else:
            words_lst.append(temp_a)
    for _ in range(len(words_lst)):
        result.append(words_lst.pop())
    for a in result:
        if 
    print(f"#{t} {result}")





