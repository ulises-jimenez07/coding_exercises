
def make_change(amount, denoms):
    return make_change_helper(amount,denoms,0)

def make_change_helper(amount,denoms, index):
    coin = denoms[index]
    if index == len(denoms)-1:
        remaining = amount % coin
        return 1 if remaining == 0  else 0
    
    ways = 0
    for amt in range(0, amount+1, coin):
        ways += make_change_helper(amount- amt,denoms, index+1)
    return ways


print(make_change(11, [ 25,10,5,1]))
