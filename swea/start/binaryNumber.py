import sys
sys.stdin = open('input.txt')
def toBinary(num):
    global i
    global result
    for j in range(3, -1, -1):
        share, num = divmod(num, 2**j)
        result = result + str(share)

for t in range(1, int(input()) + 1):
    N, hexademical = input().split()
    N = int(N)
    # ord(?) = ? - 55
    result = ""
    for i in range(len(hexademical)):
        hexad = hexademical[i]
        if hexad.isnumeric():
            hexad = int(hexad)
        else:
            hexad = ord(hexad) - 55
        toBinary(hexad)
    print(f'#{t} {result}')