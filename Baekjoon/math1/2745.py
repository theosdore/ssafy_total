# ? =  ord(?) - 55
N, B = input().split()
B = int(B)
result = 0

# j = 지수
j = 0
for i in range(len(N)-1, -1, -1):
    if N[i].isdigit():
        result += int(N[i])*(B**j)
    else:
        result += (ord(N[i])-55)*(B**j)
    j += 1

print(result)