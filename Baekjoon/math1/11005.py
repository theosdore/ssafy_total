N, B = map(int, input().split())
temp_N = N
result = []
while True:
    if temp_N < B:
        if temp_N > 9:
            result.append(chr(temp_N + 55))
            break
        else:
            result.append(str(temp_N))
            break

    temp_N, remain = divmod(temp_N, B)

    if remain > 9:
        result.append(chr(remain + 55))
    else:
        result.append(str(remain))

print(''.join(result[::-1]))
