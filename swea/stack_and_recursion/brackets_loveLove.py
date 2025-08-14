import sys
sys.stdin = open("input.txt")
for t in range(1, 11):
    brackets_dic = {
        "(": 1,
        ")": -1,
        "<": 2,
        ">": -2,
        "[": 3,
        "]": -3,
        "{": 4,
        "}": -4
    }
    num = int(input())
    result_1 = []
    for word in input():
        temp_num = brackets_dic[word]
        if temp_num > 0:
            result_1.append(temp_num)
        elif result_1.pop() + temp_num != 0:
            print(f"#{t} 0")
            break
    else:
        print(f"#{t} 1")