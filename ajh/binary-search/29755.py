# 블랙홀과 소행성
# 블랙홀 n개, 소행성 m개, 블랙홀 각각의 끌어당기는 힘은 p로 같음
# 블랙홀i의 위치 b_i, 소행성 j의 위치 a_j, 질량 w_j
# |b_i - a_j| <= p/w_j -> 블랙홀이 소행성 j를 빨아들임
# 하나가 여러개 빨아들이기 가능, 
# 여러 블랙홀이 같은 소행성을 끌어들일수있을땐 위치가 가장 왼쪽에 있는 블랙홀이 빨아들임

# 모든 소행성을 빨아들이기 위한 정수 p의 최솟값 구하기 
# w_j|b_i - a_j| <= p : w_j|b_i - a_j|가 p의 최솟값 
# 최솟값 p를 찾기 위해서는 b_i-a_j(소행성과의 거리)가 가장 작은 블랙홀들을 찾고 p 계산
# 가장 작은 p들 중 제일 큰 것 찾기 
# 한 위치에는 블랙홀만 하나 존재하거나 소행성만 하나 존재
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
blackhole = sorted(list(map(int, input().split()))) # b_i
asteroid = [tuple(map(int, input().split())) for _ in range(m)] # a_j, w_j

res = []

for a in asteroid:
    start = 0
    end = n - 1

    tmp = int(1e9)
    while start <= end:
        mid = (start + end)//2
        
        tmp = min(tmp, abs(blackhole[mid] - a[0]) * a[1])

        if blackhole[mid] < a[0]:
            start = mid + 1
        else:
            end = mid - 1
    res.append(tmp)

print(max(res))





