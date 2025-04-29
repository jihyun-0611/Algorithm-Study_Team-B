n = int(input())

memo = {}
def fibo(k):
    if k == 0 or k == 1:
        return k
    if k not in memo:
        memo[k] = fibo(k-1) + fibo(k-2)
    
    return memo[k]

print(fibo(n))