# blobnom https://www.acmicpc.net/problem/24498
import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))

# 1. 처음과 마지막이 아닌 탑 중 하나a[i]를 선택 -> a[i-1], a[i], a[i+1] >=1
# 2. a[i-1]-1, a[i+1]-1
# 3. a[i]+1

ans = [max(a)]
cur = a
for i in range(1, n-1):
    if cur[i] <= 0 or cur[i-1] <= 0 or cur[i+1] <= 0:
        continue
    select = cur[i] + min(cur[i-1], cur[i+1])
    ans.append(select)

print(max(ans))