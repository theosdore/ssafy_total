import sys
input = sys.stdin.readline
n, k = map(int,input().split())
coinlst = [int(input()) for _ in range(n)]
# 흠,,, 큰거부터 최대로 넣고 하나씩 빼는 방법
coinlst.sort()

# a < b < c 일때
# a*h >= k 가 되는 가장 작은 h를 구하고 -> k//a = h를
# h를 하나씩 줄여가고 
