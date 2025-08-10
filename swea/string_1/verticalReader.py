for t in range(1, int(input())+1):
    arr = [list(input()) for _ in range(5)]
    result = [""]
    result_len = 0
    for words in arr:
        for i in range(len(words)):
            if result_len < i:
                result.append("")
                result_len += 1
            result[i] += words[i]
    print(f"#{t} {''.join(result)}")