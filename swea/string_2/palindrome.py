# import sys
# sys.stdin = open("input.txt")
"""
큰 경우의 수 부터 조사해서 회문 나오면 멈추기
"""

def palidndorme_check(word):
    for i in range(len(word) // 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


for _ in range(1, 11):
    result = 0
    t = int(input())
    arr = [list(input()) for _ in range(100)]

    # 행 순서로 확인 시작
    end_counter = False
    result_row = 1
    for length in range(99, -1, -1):
        for row in arr:
            for k in range(100-length):
                if palidndorme_check(row[k:k+length+1]):
                    end_counter = True
                    result_row = length + 1
                    break
            if end_counter:
                break
        if end_counter:
            break

    # 열을 전치로 풀기
    transpose_arr = [[x[j] for x in arr] for j in range(100)]

    #열 순서로 확인 시작
    end_counter = False
    result_col = 1
    for length in range(99, -1, -1):
        # 행보다 작아지면 멈춰!
        if length == result_row - 1:
            break
        for row in transpose_arr:
            for k in range(100 - length):
                if palidndorme_check(row[k:k + length + 1]):
                    end_counter = True
                    result_col = length + 1
                    break
            if end_counter:
                break
        if end_counter:
            break

    # # 전치없이 풀기 (<-- 하지마셈 오래걸림)
    #
    # end_counter = False
    # result_col = 1
    # for length in range(99, -1, -1):
    #     for row_idx in range(100):
    #         for k in range(100-length):
    #             word = ""
    #             for col_idx in range(length +1):
    #                 word += arr[k+col_idx][row_idx]
    #             if palidndorme_check(word):
    #                 end_counter = True
    #                 result_col = length + 1
    #                 break
    #         if end_counter:
    #             break
    #     if end_counter:
    #         break

    result = max([result_col, result_row])
    # print(result_col, result_row)
    print(f"#{t} {result}")
