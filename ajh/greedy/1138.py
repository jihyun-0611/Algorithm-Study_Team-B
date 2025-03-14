# 한 줄로 서기 : https://www.acmicpc.net/problem/1138
# 정렬? 왼쪽에 나보다 키큰 사람밖에 없다는거? 빌딩을 생각해보자 
# 2 1 1 0 : 
# 1 - 최소 2명이 왼쪽에 있었다는것
# 2, 3 - 최소 1명이 왼쪽 그러나 모든 사람의 키가 다르므로 둘 중 하나는 
# 문제 - 키가 1인 사람부터 N까지 -> idx 가 height가 됨 

n = int(input())
people = list(map(int, input().split())) # 0<= people[i] <= n-1
line = [-1] * n
for idx, left in enumerate(people):
    height = idx + 1
    cnt = 0
    for i in range(n):
        if line[i] == -1 and cnt == people[idx]:
            line[i] = height
            break
        elif line[i] == -1: # 아직 안 채워져있다는 것은 나보다 키큰 친구의 자리가 있다는것이니까!
            cnt += 1
print(*line)