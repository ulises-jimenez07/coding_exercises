def fib_memo(n, memo):
    if n < 0:
        raise ValueError("Not supported")
    if n in [0, 1]:
        return n
    if not n in memo:
        memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_tabuluation(n):
    tb = [0, 1]
    for i in range(2, n + 1):
        tb.append(tb[i - 1] + tb[i - 2])
    return tb[n]


my_dic = {}
print(fib_memo(6, my_dic))

print(fib_tabuluation(6))
