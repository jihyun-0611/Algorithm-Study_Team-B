# MBTI 성격 유형을 이용하면 두 사람 사이의 심리적인 거리를 정의
# 이는 두 사람의 MBTI 유형에서 서로 다른 분류에 속하는 척도의 수로 정의
# MBTI 유형이 ISTJ인 사람과 ISFJ인 사람 사이의 거리는 1이며, INTP인 사람과 ENTJ인 사람 사이의 거리는 2
# A, B, C 거리 : (A와 B사이의 심리적인 거리) + (B와 C사이의 심리적인 거리) + (A와 C사이의 심리적인 거리)
# N명의 학생들의 MBTI 유형이 주어질 때, 가장 가까운 세 학생 사이의 심리적인 거리

import sys
input = sys.stdin.readline

T = int(input())

def combine(start=0, curr=[]):
    global ans
    if len(curr) == 3:
        res = 0
        for k in range(3):
            a = curr[k]
            b = curr[(k+1)%3]
            tmp = 0
            for x, y in zip(a, b):
                if x == y:
                    continue
                else:
                    tmp += 1
            res += tmp
        if ans >= res:
            ans = res
        return 
    for i in range(start, n):
        curr.append(mbti[i])
        combine(i+1, curr)
        curr.pop()

for _ in range(T):
    n = int(input())
    mbti = input().split()
    ans = int(1e9)
    if n <= 32:
        combine()
    else:
        ans = 0
    print(ans)

# +> 시간 초과 

# 해당 문제는 비둘기 집 원리에 관련되어 있는 문제 
# mbti 종류가 16개 이므로 n이 32보다 큰 경우 반드시 3개가 중복되는 경우가 생김 따라서 정답은 반드시 0임

