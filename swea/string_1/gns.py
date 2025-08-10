dic = {
    "ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4,
    "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9
}
dic2 = {
    0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR",
    5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"
}
for _ in range(1, int(input())+1):
    test_num, n = input().split()
    lst = list(input().split())
    result = [0 for _ in range(10)]

    print(test_num)
    for num in lst:
        result[dic[num]] += 1
    for i in range(10):
        print(' '.join([dic2[i]] * result[i]), end=" ")
