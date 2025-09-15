<<<<<<< Updated upstream
=======
import sys
sys.stdin = open("SSAFY_TOTAL\swea\stack_and_recursion2\input.txt")

>>>>>>> Stashed changes
for t in range(1, 11):
    N = int(input())
    arr = list(input())
    finallist = []
    simbollist = []
    for word in arr:
        if word.isnumeric():
            finallist.append(int(word))
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
    finalnumstack = []
    finalsymbolstack = []
    for tempA in finallist:
        if isinstance(tempA, int):
            finalnumstack.append(tempA)
        else:
            if tempA == "*":
                finalnumstack.append(finalnumstack.pop() * finalnumstack.pop())
            elif tempA == "+":
                finalnumstack.append(finalnumstack.pop() + finalnumstack.pop())
    print(f"#{t}", finalnumstack[0])
