# 32069 가로등
# 가로등 n개
# 위치 x의 어두운 정도는 가장 가까운 가로등까지의 거리 (|a_i-x|중 가장 작은거)
# x=0 ~L -> 총 L+1개의 x에서의 어두운 정도를 가장 작은값부터 k개 출력

import sys
from collections import deque
input = sys.stdin.readline

l, n, k = map(int, input().split())
lamps = list(map(int, input().split()))

answer = []

# L이 매우 크므로 딱 필요한 만큼만 반복하기 
q = deque()
visited = {} # x: 어두운 정도
for lamp in lamps:
    visited[lamp] = 0
    q.append((lamp, 0))

while q:
    x, dark = q.popleft()
    answer.append(dark)
    if len(answer) == k:
        break
    for v in [x-1, x+1]:
        if v < 0 or v > l :
            continue
        if v not in visited:
            q.append((v, dark+1))
            visited[v] = dark+1
answer.sort()
for a in answer:
    print(a)