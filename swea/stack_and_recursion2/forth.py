for t in range(1, int(input())+1):
    arr = input().split()
    num_stack = []
    for a in arr:
        if a.isnumeric() :
            num_stack.append(int(a))
        else:
            if len(num_stack) > 1:
                if a == "+":
                    num_stack.append(num_stack.pop() + num_stack.pop())
                elif a == "-":
                    num_stack.append(-num_stack.pop() + num_stack.pop())
                elif a == "*":
                    num_stack.append(num_stack.pop() * num_stack.pop())
                elif a =="/":
                    divin_num = num_stack.pop()
                    num_stack.append(  num_stack.pop()//divin_num)
            elif a ==".":
                print(f"#{t} {num_stack.pop()}")
                break
            else:
                print(f"#{t} error")
                break