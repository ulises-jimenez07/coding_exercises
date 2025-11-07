def triple_hop(x):
    memo = [-1] * (x + 1)
    return triple_hop_count(x, memo)


def triple_hop_count(x, memo):
    if x < 0:
        return 0
    elif x == 0:
        return 1
    elif memo[x] > -1:
        return memo[x]
    else:
        memo[x] = triple_hop_count(x - 1, memo) + triple_hop_count(x - 2, memo) + triple_hop_count(x - 3, memo)
    return memo[x]


def triple_hop2(x):
    if x < 0:
        return 0
    if x == 0:
        return 1
    if x == 1:
        return 1
    return triple_hop(x - 1) + triple_hop(x - 2) + triple_hop(x - 3)


print(triple_hop(1))
print(triple_hop(2))
print(triple_hop(3))
print(triple_hop(4))
print(triple_hop(5))
print(triple_hop(6))
