def rob_house(houses, current_house, memo):
    if current_house > len(houses) - 1:
        return 0
    if current_house in memo:
        return memo[current_house]
    steal_first_house = houses[current_house] + rob_house(houses, current_house + 2, memo)
    skip_first_house = rob_house(houses, current_house + 1, memo)
    memo[current_house] = max(steal_first_house, skip_first_house)
    return memo[current_house]


def robber_bu(houses, current_index):
    temp_arr = [0] * (len(houses) + 2)
    for i in range(len(houses) - 1, -1, -1):
        temp_arr[i] = max(houses[i] + temp_arr[i + 2], temp_arr[i + 1])
    return temp_arr[0]


def robber_bu_2(houses):
    num_houses = len(houses)
    if num_houses == 0:
        return 0
    if num_houses == 1:
        return houses[0]

    house1 = houses[0]
    house2 = max(houses[0], houses[1])
    ans = house2
    for i in range(2, num_houses):
        ans = max(house1 + houses[i], house2)
        house1 = house2
        house2 = ans
    return ans


houses = [6, 7, 1, 30, 8, 2, 4]
my_dic = {}
print(rob_house(houses, 0, my_dic))
print(robber_bu(houses, 0))
