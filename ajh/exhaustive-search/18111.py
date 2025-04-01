# 마인크래프트 18111
# 땅고르기 작업
# n, m 크기의 집터
# 1. 좌표 i, j의 맨 위 블록 제거(2초) or 2. 좌표 i, j의 맨위에 블록 올리기(1초)
# 땅 고르기 작업의 최소시간 , 땅의 높이 구하기 (여러개라면 가장 높은 것)
# 제한 : 지하 x, 집터에서만 블록 수급, 작업시작시 인벤토리에 b개, 0<=높이는 <= 256
import sys
input = sys.stdin.readline
n, m, b = map(int, input().split())
grd = [list(map(int, input().split())) for _ in range(n)]

# 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.
# 각 도달하고 싶은 높이마다 2차원 리스트를 탐색
ans = int(1e9)
height = 0

for k in range(257):
    used = 0
    taken = 0
    for i in range(n):
        for j in range(m):
            if grd[i][j] > k:
                taken += grd[i][j] - k
            else:
                used += k - grd[i][j]

    # 도달 높이로 만드는 게 가능한지 확인
    if used > taken + b:
        continue

    # 시간을 계산하고 최솟값 비교
    cnt = taken * 2 + used

    if cnt <= ans:
        ans = cnt
        height = k

print(ans, height)
    
            


# 높이 제한이 0~256으로 명시 -> 높이대로 탐색해서 시간 기록?
# time_by_height = [-1 for _ in range(257)]
# max_height = 0
# for t in range(257):
#     time = 0
#     block = b
#     for i in range(n):
#         for j in range(m):
#             tmp = -1
#             if grd[i][j] == t:
#                 continue
#             if grd[i][j] < t:
#                 tmp = t - grd[i][j]
#                 block -= (t - grd[i][j])
#             elif grd[i][j] > t:
#                 tmp = (grd[i][j] - t)*2
#                 block += (grd[i][j] - t)
#             else:
#                 time = -1
#                 time_by_height[t] = -1
#             time += tmp
#             time_by_height[t] = time

