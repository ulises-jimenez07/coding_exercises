def number_factor_memo(n, memo):
    if n in (0, 1, 2):
        return 1
    if n == 3:
        return 2
    if n in memo:
        return memo[n]
    else:
        sub_p1 = number_factor_memo(n - 1, memo)
        sub_p2 = number_factor_memo(n - 3, memo)
        sub_p3 = number_factor_memo(n - 4, memo)
        memo[n] = sub_p1 + sub_p2 + sub_p3
    return memo[n]


def number_factor_tab(n):
    tb = [1, 1, 1, 2]
    for i in range(4, n + 1):
        tb.append(tb[i - 1] + tb[i - 3] + tb[i - 4])
    return tb[n]


my_dic: dict[int, int] = {}
print(number_factor_memo(5, my_dic))
print(number_factor_tab(5))
