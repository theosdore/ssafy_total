word1, word2 = input(), input()
len1 , len2 = len(word1)+1, len(word2)+1

arr = [[0]*(len2) for _ in range(len1)]
# i,j == 0 일 땐 0으로 초기화 (공집합 부분수열)
for i in range(1, len1):
    for j in range(1, len2):
        # i 그대로 놓고 j 키워가면서 word1의 i번째까지 부분수열중에 word2의 j번째 부분수열과 겹치는 최대길이 찾기
        if word1[i-1] == word2[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
            
maxlen = arr[-1][-1]

print(maxlen)
if maxlen != 0:
    lcs_string = []
    # 0 도착하면 멈춤
    while arr[len1-1][len2-1] > 0:
        # 두 글자 같으면 정답에 추가, 대각선 뒤로 이동
        # -2 하는 이유는 len = 단어 길이 + 1. arr은 0~ 단어길이. 단어 인덱싱은 0~단어길이 -1 -> len-2
        if word1[len1-2]==word2[len2-2]:
            lcs_string.append(word1[len1-2])
            len1 -= 1
            len2 -= 1
            
        else:
            # 더 큰 방향으로 이동
            if arr[len1-2][len2-1] > arr[len1-1][len2-2]:
                len1 -= 1
            else:
                len2 -= 1
                
    print(''.join(reversed(lcs_string)))