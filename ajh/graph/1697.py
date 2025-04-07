# 숨바꼭질
# 수빈이 n, 동생 k (0<=n, k<=10^5)
# 걷기 :  1초 후 x-1 or x+1
# 순간이동 : 1초 후 2*x
# 가장 빨리 찾는 시간
from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

# 이동 방식: -1, +1, *2
d = [2, 1, -1]

q = deque()
visited = [0 for _ in range(100001)]

q.append((n, 0))
visited[n] = 1
while q:
    cur_v, cur_t = q.popleft()
    if cur_v == k:
        print(cur_t)
        break
    
    for i in d:
        nxt = 0
        if i == 2:
            nxt = cur_v*2
        else:
            nxt = cur_v+i
        if 0 <= nxt< 100001 and visited[nxt] == 0:
            q.append((nxt, cur_t+1))
            visited[nxt] = 1
# -> 시간 초과 : 딕셔너리? -> 메모리 초과 : 
# 미리 배열길이에 맞게 생성 후 next node가 범위에 맞게 있는지 확인 - 인덱스에러 방지


