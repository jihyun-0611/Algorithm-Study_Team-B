# 00 또는 1
# 1 <= n <= 1000000 : o(n) 또는 o(logn)
# n=1 -> 1, n=2 -> 2
# n=3 -> ---: 100, 001, 111 n=4 -> 0011, 0000, 1001, 1100, 1111 
# n=5  -> ----- : 11111, 00111(4), 00001(3) - 00이 몇개 들어갈지 (0~n//2) (각 00이 k개일때의 위치 : )
# 규칙 : 피보나치

import sys
input = sys.stdin.readline

n = int(input())

# memo = {}
# def fib(num):
#     if num == 1 or num == 2:
#         return num
#     if num not in memo:
#         memo[num] = fib(num-1) + fib(num-2)
#     return memo[num] => RecursionError발생
# res = fib(n)
#=> RecursionError발생, 딕셔너리 사용시 메모리 초과
memo = [0]*(n+1)
for i in range(1, n+1):
    if i == 1 or i == 2:
        memo[i] = i
        continue
    memo[i] = (memo[i-1] + memo[i-2])%15746 # 나머지 연산후 저장 -> 메모리 효율

# 15746 으로 나눈 나머지 출력
print(memo[n])
# memo[1]과 memo[2]를 루프 밖에서 정했을 때 n=1일때 인덱스 에러 발생함 