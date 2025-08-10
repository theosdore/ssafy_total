
# i = 2 ~ N -2
# i-2, i-1, i+1, i+2 를 i와 비교
# 최솟값을 구하고 최솟값이 0보다 클 때 세대수 +1

def sight_count(bc, bh):
    counts_total = 0
    for k in range(2, bc-2):
        maxi = 0
        for j in [-2, -1, 1, 2]:
            if bh[k + j] > maxi:
                maxi = bh[k+j]
        if bh[k] > maxi:
            counts_total += bh[k] - maxi
    return counts_total


for i in range(10):
    building_counts = int(input())
    building_heights = list(map(int, input().split()))
    total_counts = sight_count(building_counts, building_heights)
    print(f"#{i + 1} {total_counts}")