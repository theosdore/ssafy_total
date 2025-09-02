import sys
sys.stdin = open("ssafy_total\swea\stack_and_recursion2\input.txt")
for t in range(1, 11):
    N = int(input())
    arr = list(input())
    finallist = []
    simbollist = []
    for word in arr:
        if word.isnumeric():
            finallist.append(word)
        else:
            if word == ")":
                while simbollist[-1] != "(":
                    finallist.append(simbollist.pop())
                simbollist.pop()
            elif word == "+":
                while simbollist and simbollist[-1] != "(":
                    finallist.append(simbollist.pop())
                simbollist.append(word)
            else: 
                simbollist.append(word)
    while simbollist:
        finallist.append(simbollist.pop())
    print(f"#{t}", ''.join(finallist))

